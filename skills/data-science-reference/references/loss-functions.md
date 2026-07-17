# Loss Functions

Consolidated from multiple overlapping source sheets — this is the deduplicated version.

## Regression losses

| Loss | Formula | Behavior | Outlier sensitivity |
|---|---|---|---|
| Mean Bias Error (MBE) | (1/N)Σ(yᵢ−ŷᵢ) | Captures directional bias only; rarely used to train | Low, but cancels +/- errors |
| MAE (L1) | (1/N)Σ\|yᵢ−ŷᵢ\| | Average absolute error | Low — robust |
| MSE (L2) | (1/N)Σ(yᵢ−ŷᵢ)² | Average squared error | High — penalizes large errors heavily |
| RMSE | √MSE | Same units as target variable | High |
| Huber Loss | Quadratic below threshold δ, linear above | Combines MSE (small errors) + MAE (large errors) | Medium — tunable via δ |
| Log-Cosh | (1/N)Σlog(cosh(ŷᵢ−yᵢ)) | Smooth MAE-like alternative | Low, more compute cost |
| Quantile (Pinball) Loss | τ(y−ŷ) if y≥ŷ else (1−τ)(ŷ−y) | Predicts a specific quantile (τ=0.5 → median) | Low |
| Poisson Loss | ŷ − y·log(ŷ) | For count/event data | Medium |

## Classification losses

| Loss | Formula | Behavior | Use case |
|---|---|---|---|
| Binary Cross-Entropy (Log Loss) | −(1/N)Σ[yᵢlog(pᵢ)+(1−yᵢ)log(1−pᵢ)] | Standard binary classifier loss | Binary classification |
| Cross-Entropy (multi-class) | −(1/N)ΣᵢΣ_c y_ic·log(p_ic) | Extension of BCE to C classes | Multi-class classification, deep nets |
| Hinge Loss | (1/N)Σmax(0, 1−yᵢf(xᵢ)) | Margin-based, y∈{−1,+1} | SVMs |
| Squared Hinge | (1/N)Σmax(0, 1−yᵢf(xᵢ))² | Smoother gradient, penalizes misclassification harder | SVM variants |
| Focal Loss | −α(1−pₜ)^γ·log(pₜ) | Down-weights easy examples, focuses on hard ones | Class imbalance, object detection |
| KL Divergence | ΣP(i)log(P(i)/Q(i)) | Measures distribution mismatch | VAEs, distillation, probabilistic models |

## Selection guide

| Situation | Use |
|---|---|
| Standard regression | MSE |
| Regression with outliers you don't want to dominate the loss | MAE or Huber |
| Need error in the original units for reporting | RMSE |
| Want smooth gradients + outlier robustness | Log-Cosh |
| Binary classification | Binary Cross-Entropy |
| Multi-class classification | Cross-Entropy |
| Support Vector Machine | Hinge Loss |
| Severely imbalanced classes (e.g., fraud, rare defects) | Focal Loss |
| Comparing two probability distributions (e.g., VAE latent vs prior) | KL Divergence |
| Predicting a range/interval, not a point | Quantile Loss |
| Count data (arrivals, occurrences) | Poisson Loss |

## Gotcha

MSE and RMSE look interchangeable but aren't for reporting — RMSE is in the target's original units (e.g., pesos, days) and is what you want in front of a non-technical stakeholder; MSE is squared units and only useful for optimization/comparison.
