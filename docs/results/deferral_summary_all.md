# Deferral study: all runs

Adaptive-attacker ASR (share of attacked toxic texts allowed). Where several seeds of a setting exist, values are mean ± std across seeds.

| Signal | Primary | Benign source | Seeds | Attacked | Budget | Review rate (test) | Attack | ASR, no band | ASR, adaptive with band |
|---|---|---|---|---|---|---|---|---|---|
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 0% | 0.0% | char | 10.5% | 10.5% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 0% | 0.0% | word | 31.5% | 31.5% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 0% | 0.0% | genetic | 18.8% | 18.8% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 5% | 4.0% | char | 10.5% | 5.5% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 5% | 4.0% | word | 31.5% | 26.0% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 5% | 4.0% | genetic | 18.8% | 14.4% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 10% | 6.0% | char | 10.5% | 1.7% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 10% | 6.0% | word | 31.5% | 15.5% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 10% | 6.0% | genetic | 18.8% | 6.1% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 20% | 16.0% | char | 10.5% | 0.0% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 20% | 16.0% | word | 31.5% | 9.9% |
| ensemble | unitary/toxic-bert | jigsaw | 1 | 181 | 20% | 16.0% | genetic | 18.8% | 3.3% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 0% | 0.0% | char | 65.7% | 65.7% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 0% | 0.0% | word | 41.2% | 41.2% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 0% | 0.0% | genetic | 37.2% | 37.2% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 5% | 3.0% | char | 65.7% | 27.5% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 5% | 3.0% | word | 41.2% | 26.5% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 5% | 3.0% | genetic | 37.2% | 20.6% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 10% | 9.0% | char | 65.7% | 16.7% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 10% | 9.0% | word | 41.2% | 20.6% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 10% | 9.0% | genetic | 37.2% | 19.6% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 20% | 16.0% | char | 65.7% | 7.8% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 20% | 16.0% | word | 41.2% | 9.8% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw | 1 | 102 | 20% | 16.0% | genetic | 37.2% | 14.7% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 0% | 0.0% | char | 65.7% | 65.7% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 0% | 0.0% | word | 38.2% | 38.2% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 0% | 0.0% | genetic | 38.2% | 38.2% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 5% | 4.0% | char | 65.7% | 55.9% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 5% | 4.0% | word | 38.2% | 33.3% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 5% | 4.0% | genetic | 38.2% | 33.3% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 10% | 7.5% | char | 65.7% | 49.0% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 10% | 7.5% | word | 38.2% | 27.5% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 10% | 7.5% | genetic | 38.2% | 32.4% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 20% | 15.5% | char | 65.7% | 36.3% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 20% | 15.5% | word | 38.2% | 24.5% |
| single | facebook/roberta-hate-speech-dynabench-r4-target | jigsaw_hard | 1 | 102 | 20% | 15.5% | genetic | 38.2% | 28.4% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 0% | 0.0% | char | 33.9% | 33.9% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 0% | 0.0% | word | 44.9% | 44.9% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 0% | 0.0% | genetic | 33.1% | 33.1% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 5% | 6.0% | char | 33.9% | 12.7% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 5% | 6.0% | word | 44.9% | 24.6% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 5% | 6.0% | genetic | 33.1% | 11.9% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 10% | 7.0% | char | 33.9% | 9.3% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 10% | 7.0% | word | 44.9% | 20.3% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 10% | 7.0% | genetic | 33.1% | 9.3% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 20% | 14.0% | char | 33.9% | 3.4% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 20% | 14.0% | word | 44.9% | 11.9% |
| single | martin-ha/toxic-comment-model | jigsaw | 1 | 118 | 20% | 14.0% | genetic | 33.1% | 5.9% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 0% | 0.0% | char | 33.9% | 33.9% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 0% | 0.0% | word | 44.9% | 44.9% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 0% | 0.0% | genetic | 34.8% | 34.8% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 5% | 3.0% | char | 33.9% | 30.5% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 5% | 3.0% | word | 44.9% | 43.2% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 5% | 3.0% | genetic | 34.8% | 28.8% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 10% | 7.0% | char | 33.9% | 28.0% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 10% | 7.0% | word | 44.9% | 41.5% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 10% | 7.0% | genetic | 34.8% | 25.4% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 20% | 16.0% | char | 33.9% | 19.5% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 20% | 16.0% | word | 44.9% | 37.3% |
| single | martin-ha/toxic-comment-model | jigsaw_hard | 1 | 118 | 20% | 16.0% | genetic | 34.8% | 21.2% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 0% | 0.0% | char | 10.5% | 10.5% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 0% | 0.0% | word | 36.5% | 36.5% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 0% | 0.0% | genetic | 17.7% | 17.7% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 5% | 3.5% | char | 10.5% | 8.8% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 5% | 3.5% | word | 36.5% | 33.1% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 5% | 3.5% | genetic | 17.7% | 14.4% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 10% | 7.5% | char | 10.5% | 5.5% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 10% | 7.5% | word | 36.5% | 29.8% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 10% | 7.5% | genetic | 17.7% | 13.8% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 20% | 16.5% | char | 10.5% | 3.3% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 20% | 16.5% | word | 36.5% | 20.4% |
| single | unitary/toxic-bert | hatexplain | 1 | 181 | 20% | 16.5% | genetic | 17.7% | 7.2% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 0% | 0.0 ± 0.0% | char | 10.8 ± 2.0% | 10.8 ± 2.0% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 0% | 0.0 ± 0.0% | word | 31.8 ± 3.0% | 31.8 ± 3.0% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 0% | 0.0 ± 0.0% | genetic | 16.2 ± 2.7% | 16.2 ± 2.7% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 5% | 3.0 ± 0.8% | char | 10.8 ± 2.0% | 2.9 ± 0.9% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 5% | 3.0 ± 0.8% | word | 31.8 ± 3.0% | 13.4 ± 3.2% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 5% | 3.0 ± 0.8% | genetic | 16.2 ± 2.7% | 6.0 ± 0.7% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 10% | 5.7 ± 0.5% | char | 10.8 ± 2.0% | 1.8 ± 1.2% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 10% | 5.7 ± 0.5% | word | 31.8 ± 3.0% | 9.6 ± 3.3% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 10% | 5.7 ± 0.5% | genetic | 16.2 ± 2.7% | 3.7 ± 0.3% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 20% | 15.3 ± 2.5% | char | 10.8 ± 2.0% | 0.7 ± 0.7% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 20% | 15.3 ± 2.5% | word | 31.8 ± 3.0% | 5.1 ± 1.5% |
| single | unitary/toxic-bert | jigsaw | 3 | 181/179/185 | 20% | 15.3 ± 2.5% | genetic | 16.2 ± 2.7% | 1.7 ± 0.5% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 0% | 0.0% | char | 10.5% | 10.5% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 0% | 0.0% | word | 34.8% | 34.8% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 0% | 0.0% | genetic | 18.2% | 18.2% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 5% | 4.5% | char | 10.5% | 5.5% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 5% | 4.5% | word | 34.8% | 23.8% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 5% | 4.5% | genetic | 18.2% | 9.4% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 10% | 9.0% | char | 10.5% | 3.9% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 10% | 9.0% | word | 34.8% | 18.8% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 10% | 9.0% | genetic | 18.2% | 7.2% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 20% | 18.0% | char | 10.5% | 2.8% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 20% | 18.0% | word | 34.8% | 15.5% |
| single | unitary/toxic-bert | jigsaw_hard | 1 | 181 | 20% | 18.0% | genetic | 18.2% | 5.5% |
