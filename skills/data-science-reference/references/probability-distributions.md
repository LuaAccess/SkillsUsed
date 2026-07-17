# Probability Distributions

Consolidated from multiple source sheets; duplicates removed, notation reconciled.

## Discrete

| Distribution | Params | Formula | Notes | Use case |
|---|---|---|---|---|
| **Bernoulli** | p | P(X=x) | Single trial, 2 outcomes; Binomial with n=1 | Binary classification, coin toss |
| **Binomial** | n, p | P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ | Mean=np, Var=np(1−p) | Conversion rates, A/B testing, click-through |
| **Multinomial** | n, x1..xk, p1..pk | n!/(x1!...xk!) · Πpᵢ^xᵢ | Generalizes Binomial to >2 categories | Multi-class classification, text generation |
| **Geometric** | p | n=1 case of Negative Binomial | Memoryless | Waiting-time-to-first-success problems |
| **Negative Binomial** | r, p | — | Number of trials until r-th success | Overdispersed count data, insurance |
| **Poisson** | λ | P(X=k) = e^(−λ)λᵏ/k! | λ = np as n→∞; mean=variance=λ | Arrivals, accidents, network traffic, event counts |
| **Hypergeometric** | N, K, n | — | Sampling *without* replacement; ≈Binomial when n/N ≤ 0.05 | Card games, quality inspection, small-population sampling |

## Continuous

| Distribution | Params | Formula | Notes | Use case |
|---|---|---|---|---|
| **Uniform** | a, b | f(x)=1/(b−a) | All outcomes equally likely | Random sampling, Monte Carlo |
| **Normal (Gaussian)** | μ, σ² | f(x)=(1/(σ√2π))e^(−(x−μ)²/2σ²) | Most important distribution in stats — CLT convergence target | Hypothesis testing, measurement error, ML feature modeling |
| **Multivariate Normal** | μ (vector), Σ (cov matrix) | f(x)=(1/((2π)^(d/2)\|Σ\|^½))·exp(−½(x−μ)ᵀΣ⁻¹(x−μ)) | Extends Normal to d dimensions | GMMs, VAEs, anomaly detection |
| **Lognormal** | μ, σ² | if ln(X)~N(μ,σ²) | Right-skewed, always positive | Stock prices, income distributions |
| **t-Distribution** | df | t = Z/√(V/df) | Heavier tails than Normal; converges to Normal as df→∞ | Small-sample t-tests, confidence intervals |
| **Chi-Squared** | k (df) | χ²(k) = Σ Zᵢ² | Sum of squared standard normals | Goodness-of-fit, independence testing, feature selection |
| **Gamma** | k (shape), θ (scale) | f(x)=x^(k−1)e^(−x/θ)/(θᵏΓ(k)) | Generalizes Exponential; models waiting time to k-th event | Bayesian inference, reliability/survival analysis |
| **Exponential** | λ | k=1 case of Gamma | Memoryless; models time between Poisson events | Queueing, survival analysis |
| **Weibull** | k, λ | — | Becomes Exponential when k=1 | Failure-time / reliability engineering |
| **Beta** | α, β | f(x)=x^(α−1)(1−x)^(β−1)/B(α,β), 0<x<1 | Symmetric when α=β (not Normal) | Bayesian A/B testing, conversion rate modeling |
| **Dirichlet** | α (vector) | f(x)=(1/B(α))·Πxᵢ^(αᵢ−1) | Multivariate generalization of Beta; x on the simplex | Topic modeling (LDA), multi-class probability modeling |
| **Cauchy (standard)** | (0,1) | X1/X2 of two standard normals | Heavy-tailed; mean and variance undefined | Robust statistics, adversarial/pathological examples |

## Relationships (how they connect)

- Bernoulli → Binomial (n=1 case)
- Binomial → Poisson as n→∞, p→0, np=λ fixed
- Binomial → Normal as n→∞ with p fixed (μ=np, σ²=np(1−p))
- Poisson → Exponential (time *between* Poisson events)
- Exponential → Gamma (Exponential is Gamma with shape=1)
- Weibull → Exponential when shape k=1
- Normal → Lognormal (X is Lognormal if ln(X) is Normal)
- Normal → Chi-Squared (sum of squared standard normals)
- Beta(1,1) = Uniform(0,1)

## Quick selection guide

| Problem | Distribution |
|---|---|
| Binary outcome | Bernoulli |
| Number of successes in n trials | Binomial |
| Number of events in fixed interval | Poisson |
| Waiting time to first event | Exponential |
| Waiting time to k-th event | Gamma |
| Continuous, symmetric, natural data | Normal |
| Positive, right-skewed data (income, prices) | Lognormal |
| Modeling a probability itself (0–1) | Beta |
| Modeling probabilities across >2 categories | Dirichlet |
| Sampling without replacement | Hypergeometric |
| Reliability / time-to-failure | Weibull |
| Small-sample inference | t-Distribution |
| Testing independence / goodness-of-fit | Chi-Squared |

## Interview favorites

Normal, Binomial, Poisson, Exponential, Gamma, Beta, Chi-Squared, Weibull, Lognormal, Cauchy — these come up disproportionately often in data science interviews; know the mean/variance and one real use case for each cold.
