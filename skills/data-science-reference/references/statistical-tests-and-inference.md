# Statistical Tests & Inferential Statistics

## Core inferential concepts

**Central Limit Theorem (CLT):** regardless of the population's distribution shape, the sampling distribution of the mean approaches Normal as n grows. This is *why* so many tests below can assume normality even when raw data isn't normal.

**Confidence Interval:** a range likely to contain the true population parameter. A 95% CI means: if you repeated the sampling process many times, ~95% of the resulting intervals would contain the true mean. Common levels: 90% (α=0.10), 95% (α=0.05), 99% (α=0.01).

**Hypothesis Testing:** H0 (null, default assumption of no effect) vs H1 (alternative, evidence of an effect).
- **Type I Error (α):** rejecting a true H0 (false positive)
- **Type II Error (β):** failing to reject a false H0 (false negative)

## Test selection guide

| Goal | Data type | # Groups | Test |
|---|---|---|---|
| Compare two independent means | Continuous | 2 | Independent T-Test |
| Compare two paired measurements | Continuous | 2 (paired) | Paired T-Test |
| Compare sample mean to known population value | Continuous, σ known, n≥30 | 1 | Z-Test |
| Compare 3+ group means | Continuous, ~normal | 3+ | ANOVA |
| Compare 2 non-normal/ordinal groups | Ordinal / non-normal | 2 | Mann-Whitney U |
| Compare 3+ non-normal/ordinal groups | Ordinal / non-normal | 3+ | Kruskal-Wallis |
| Test association between categorical variables | Categorical | any | Chi-Square |
| Same, but small sample / expected cell count < 5 | Categorical | any | Fisher's Exact Test |
| Compare paired non-normal data | Paired | 2 | Wilcoxon Test |
| Measure linear relationship between two continuous vars | Continuous | 2 vars | Pearson Correlation |
| Same, but non-linear/non-normal | Ordinal | 2 vars | Spearman Correlation |

## Parametric vs non-parametric pairs

| Parametric | Non-parametric alternative |
|---|---|
| Independent T-Test | Mann-Whitney U |
| Paired T-Test | Wilcoxon |
| ANOVA | Kruskal-Wallis |
| Pearson Correlation | Spearman Correlation |

## Decision flow

```
What is your goal?
├── Compare groups
│   ├── 2 groups → T-Test (or Mann-Whitney/Wilcoxon if non-normal)
│   └── 3+ groups → ANOVA (or Kruskal-Wallis if non-normal)
└── Find relationship
    ├── Continuous vars → Pearson Correlation / Regression
    └── Categorical vars → Chi-Square (or Fisher's Exact if small n)
```

## ANOVA F-ratio

F = Variance Between Groups / Variance Within Groups. Large F → groups significantly differ.

## Regression as inference

y = β0 + β1x + ε — used for prediction, forecasting, and understanding how X affects Y. Positive/negative/zero correlation describe direction; covariance describes direction only (not standardized strength — that's what correlation adds).

## Gotcha

A statistically significant result (small p-value) is not automatically a *practically* significant one — especially with large n, trivial effects become "significant." Always pair a test result with an effect size or confidence interval before it goes into a client deliverable (relevant for BSP-adjacent reporting where a regulator may scrutinize the claim).
