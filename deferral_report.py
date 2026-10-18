"""
Turns deferral_study.py result files into
  * one trade-off figure per run: attack success vs. human-review rate,
    adaptive vs. standard attacker, one panel per attack
    (results/figures/deferral_tradeoff_<tag>.png)
  * one combined markdown table across every run, with seeds pooled into
    mean ± std where several seeds of the same setting exist
    (results/deferral_summary_all.md)

Usage:
    python deferral_report.py                       # all results/deferral_results_*.json
    python deferral_report.py results/deferral_results_single.json
"""

import argparse
import glob
import json
import os
from collections import defaultdict

import config
from stats import seed_variance_summary

# Validated two-slot categorical palette (blue, orange) on the light surface.
SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT_2 = "#52514e"
GRID = "#e6e5e0"
ADAPTIVE = "#2a78d6"
STANDARD = "#eb6834"

SUMMARY_ALL_PATH = os.path.join(config.RESULTS_DIR, "deferral_summary_all.md")

# Benign sources, in fixed slot order (validated all-pairs: blue, orange, aqua).
BENIGN_STYLE = {
    "jigsaw":      ("#2a78d6", "o", "Mild (Jigsaw)"),
    "jigsaw_hard": ("#eb6834", "s", "Strong language (Jigsaw)"),
    "hatexplain":  ("#1baf7a", "D", "Other platform (HateXplain)"),
}
SHORT_MODEL = {
    "unitary/toxic-bert": "toxic-bert",
    "martin-ha/toxic-comment-model": "toxic-comment DistilBERT",
    "facebook/roberta-hate-speech-dynabench-r4-target": "RoBERTa hate-speech",
}


def load_runs(paths):
    runs = []
    for p in paths:
        with open(p) as f:
            r = json.load(f)
        r["_path"] = p
        r["_tag"] = os.path.basename(p).replace("deferral_results_", "").replace(".json", "")
        runs.append(r)
    return runs


def _setting(run):
    c = run["config"]
    return (c.get("signal", "single"), c.get("primary", "unitary/toxic-bert"),
            c.get("benign_source", "jigsaw"))


def plot_run(run, out_path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    attacks = run["config"]["attacks"]
    budgets = run["by_budget"]
    fig, axes = plt.subplots(1, len(attacks), figsize=(4.2 * len(attacks), 3.8),
                             sharey=True, facecolor=SURFACE)
    if len(attacks) == 1:
        axes = [axes]

    # Shared y-scale sized to the largest value in ANY panel (incl. CI tops),
    # so no panel is clipped.
    y_top = max(
        100 * max(e["attacks"][a]["adaptive_attack_asr_with_band"]["ci_high"],
                  e["attacks"][a]["standard_attack_asr_with_band"]["asr"])
        for e in budgets for a in attacks
    )
    y_top = max(5.0, y_top * 1.12)

    for ax, a in zip(axes, attacks):
        ax.set_facecolor(SURFACE)
        xs, adp, lo, hi, std = [], [], [], [], []
        for e in budgets:
            rr = e["test_benign_review_rate"]["asr"]
            s = e["attacks"][a]
            xs.append(100 * (rr or 0.0))
            ad = s["adaptive_attack_asr_with_band"]
            adp.append(100 * ad["asr"])
            lo.append(100 * (ad["asr"] - ad["ci_low"]))
            hi.append(100 * (ad["ci_high"] - ad["asr"]))
            std.append(100 * s["standard_attack_asr_with_band"]["asr"])

        ax.plot(xs, std, color=STANDARD, lw=2, ls="--", marker="o", ms=6, zorder=2,
                markeredgecolor=SURFACE, markeredgewidth=1.5, label="Standard attacker")
        ax.errorbar(xs, adp, yerr=[lo, hi], color=ADAPTIVE, lw=2, marker="o", ms=7,
                    capsize=0, elinewidth=1.5, zorder=3, markeredgecolor=SURFACE,
                    markeredgewidth=1.5, label="Adaptive attacker")
        # Direct labels on the first and last adaptive points only.
        for i in (0, len(xs) - 1):
            ax.annotate(f"{adp[i]:.1f}%", (xs[i], adp[i]), textcoords="offset points",
                        xytext=(8, 4), fontsize=9, color=TEXT)

        ax.set_title({"char": "Character", "word": "Word substitution",
                      "genetic": "Genetic", "paraphrase": "Paraphrase"}.get(a, a),
                     fontsize=11, color=TEXT, loc="left")
        ax.set_xlabel("Benign texts sent to review (%)", fontsize=9, color=TEXT_2)
        ax.grid(axis="y", color=GRID, lw=1)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
        ax.tick_params(colors=TEXT_2, labelsize=9)
        ax.set_xlim(left=-1)
        ax.set_ylim(0, y_top)

    axes[0].set_ylabel("Attacks that get through (%)", fontsize=9, color=TEXT_2)
    axes[-1].legend(frameon=False, fontsize=9, loc="upper right", labelcolor=TEXT)
    sig, prim, ben = _setting(run)
    c = run["config"]
    fig.suptitle(f"Attack success vs. human-review cost · {prim} · {sig} signal · benign: {ben} · "
                 f"n={c['n_attack_targets']} attacked, 95% CI on adaptive",
                 fontsize=10, color=TEXT_2, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path, dpi=160, facecolor=SURFACE)
    plt.close(fig)


def plot_robustness(runs, out_path, attack="word", seed=None):
    """
    One panel per classifier: adaptive-attacker ASR for `attack` against the
    realized benign review rate, one line per benign source. Shows whether the
    band's value survives harder benign traffic. Single-signal runs only;
    uses `seed` (default: config.RANDOM_SEED) so every line is comparable.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    seed = config.RANDOM_SEED if seed is None else seed
    by_model = defaultdict(dict)
    for r in runs:
        c = r["config"]
        if c.get("signal", "single") != "single" or c.get("seed", seed) != seed:
            continue
        if attack not in c["attacks"]:
            continue
        by_model[c.get("primary", "unitary/toxic-bert")][c.get("benign_source", "jigsaw")] = r
    models = [m for m in SHORT_MODEL if m in by_model] + [m for m in by_model if m not in SHORT_MODEL]
    if not models:
        return None

    y_top = 0.0
    for m in models:
        for r in by_model[m].values():
            for e in r["by_budget"]:
                y_top = max(y_top, 100 * e["attacks"][attack]["adaptive_attack_asr_with_band"]["ci_high"])
    y_top = max(5.0, y_top * 1.08)

    fig, axes = plt.subplots(1, len(models), figsize=(4.3 * len(models), 4.0), sharey=True,
                             facecolor=SURFACE)
    if len(models) == 1:
        axes = [axes]
    for ax, m in zip(axes, models):
        ax.set_facecolor(SURFACE)
        for src in BENIGN_STYLE:
            if src not in by_model[m]:
                continue
            color, marker, label = BENIGN_STYLE[src]
            r = by_model[m][src]
            xs = [100 * (e["test_benign_review_rate"]["asr"] or 0.0) for e in r["by_budget"]]
            ad = [e["attacks"][attack]["adaptive_attack_asr_with_band"] for e in r["by_budget"]]
            ys = [100 * a["asr"] for a in ad]
            lo = [100 * (a["asr"] - a["ci_low"]) for a in ad]
            hi = [100 * (a["ci_high"] - a["asr"]) for a in ad]
            ax.errorbar(xs, ys, yerr=[lo, hi], color=color, lw=2, marker=marker, ms=7,
                        capsize=0, elinewidth=1.2, alpha=0.95, markeredgecolor=SURFACE,
                        markeredgewidth=1.5, label=label, zorder=3)
            ax.annotate(f"{ys[-1]:.0f}%", (xs[-1], ys[-1]), textcoords="offset points",
                        xytext=(7, -3), fontsize=9, color=TEXT)
        ax.set_title(SHORT_MODEL.get(m, m), fontsize=11, color=TEXT, loc="left")
        ax.set_xlabel("Benign texts sent to review (%)", fontsize=9, color=TEXT_2)
        ax.grid(axis="y", color=GRID, lw=1)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
        ax.tick_params(colors=TEXT_2, labelsize=9)
        ax.set_xlim(-1, 22)
        ax.set_ylim(0, y_top)
    axes[0].set_ylabel("Attacks that get through (%)", fontsize=9, color=TEXT_2)
    handles, labels = [], []
    for ax in axes:
        for h, l in zip(*ax.get_legend_handles_labels()):
            if l not in labels:
                handles.append(h); labels.append(l)
    fig.legend(handles, labels, loc="lower center", ncol=len(labels), frameon=False,
               fontsize=9, labelcolor=TEXT, title="Benign traffic the band is calibrated on",
               title_fontsize=9)
    name = {"char": "character", "word": "word-substitution", "genetic": "genetic"}.get(attack, attack)
    fig.suptitle(f"Adaptive {name} attack vs. human-review cost, by classifier and benign traffic "
                 f"(seed {seed}, 95% CI)", fontsize=10, color=TEXT_2, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0.12, 1, 0.94))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path, dpi=160, facecolor=SURFACE)
    plt.close(fig)
    return out_path


def _pct(x):
    return "n/a" if x is None else f"{100 * x:.1f}%"


def combined_table(runs) -> str:
    groups = defaultdict(list)
    for r in runs:
        groups[_setting(r)].append(r)

    lines = ["# Deferral study: all runs\n",
             "Adaptive-attacker ASR (share of attacked toxic texts allowed). Where several "
             "seeds of a setting exist, values are mean ± std across seeds.\n",
             "| Signal | Primary | Benign source | Seeds | Attacked | Budget | Review rate (test) | "
             "Attack | ASR, no band | ASR, adaptive with band |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for (sig, prim, ben), rs in sorted(groups.items()):
        seeds = sorted({r["config"].get("seed") for r in rs})
        n_att = "/".join(str(r["config"]["n_attack_targets"]) for r in rs)
        budgets = [e["review_budget"] for e in rs[0]["by_budget"]]
        for bi, B in enumerate(budgets):
            rr = [r["by_budget"][bi]["test_benign_review_rate"]["asr"] for r in rs]
            for a in rs[0]["config"]["attacks"]:
                nb = [r["by_budget"][bi]["attacks"][a]["binary_asr_no_band"]["asr"] for r in rs]
                ad = [r["by_budget"][bi]["attacks"][a]["adaptive_attack_asr_with_band"]["asr"] for r in rs]

                def fmt(vals):
                    vals = [v for v in vals if v is not None]
                    if not vals:
                        return "n/a"
                    if len(vals) == 1:
                        return _pct(vals[0])
                    s = seed_variance_summary(vals)
                    return f"{100 * s['mean']:.1f} ± {100 * s['std']:.1f}%"

                lines.append(f"| {sig} | {prim} | {ben} | {len(seeds)} | {n_att} | {B:.0%} | "
                             f"{fmt(rr)} | {a} | {fmt(nb)} | {fmt(ad)} |")
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("paths", nargs="*")
    args = p.parse_args()
    paths = args.paths or sorted(glob.glob(os.path.join(config.RESULTS_DIR, "deferral_results_*.json")))
    if not paths:
        raise SystemExit("no deferral_results_*.json files found; run deferral_study.py first")
    runs = load_runs(paths)
    for r in runs:
        out = os.path.join(config.FIGURES_DIR, f"deferral_tradeoff_{r['_tag']}.png")
        plot_run(r, out)
        print(f"figure: {out}")
    for att in ("word", "char"):
        out = plot_robustness(runs, os.path.join(config.FIGURES_DIR, f"deferral_robustness_{att}.png"),
                              attack=att)
        if out:
            print(f"figure: {out}")
    table = combined_table(runs)
    os.makedirs(config.RESULTS_DIR, exist_ok=True)
    with open(SUMMARY_ALL_PATH, "w") as f:
        f.write(table)
    print(table)
    print(f"combined table: {SUMMARY_ALL_PATH}")


if __name__ == "__main__":
    main()
