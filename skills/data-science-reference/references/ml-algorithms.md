# Machine Learning Algorithms

## Regression

| Algorithm | When to use | Key trait |
|---|---|---|
| Linear Regression | Simple baseline, approx-linear relationship | Fast, interpretable |
| Ridge (L2) | Multicollinearity, many features | Shrinks coefficients, doesn't zero them out |
| Lasso (L1) | Need automatic feature selection | Drives some coefficients to exactly 0 |
| Elastic Net (L1+L2) | Correlated features + need selection | Combines Ridge + Lasso strengths |
| Support Vector Regression (SVR) | Non-linear relationships, medium datasets | Kernel trick, margin-based |
| Random Forest Regressor | Non-linear tabular data, want a robust baseline | Handles interactions automatically, robust to outliers |
| XGBoost / GBM | Best raw accuracy on tabular data | Sequential error correction, needs tuning |
| Quantile Regression | Need a prediction range, not just a point estimate | Predicts conditional quantiles |

## Classification

| Algorithm | When to use | Key trait |
|---|---|---|
| Logistic Regression | Binary outcome, want interpretability | Linear decision boundary, probabilistic |
| Naive Bayes | Text/spam classification | Assumes feature independence, very fast |
| SVM | Clear margin between classes, medium data | Kernel trick for non-linear boundaries |
| Decision Tree | Need explainability | Prone to overfitting alone |
| Random Forest | General-purpose tabular classifier | Ensemble of trees, reduces overfitting |
| KNN | Simple, small dataset, similarity-based | No training phase, slow at inference |
| Gradient Boosting (XGBoost/LightGBM/CatBoost) | Competitions, best tabular accuracy | Sequential boosting, feature importance |

## Clustering (unsupervised)

| Algorithm | When to use |
|---|---|
| K-Means | Known/assumed number of roughly spherical clusters |
| Hierarchical Clustering | Want a dendrogram / nested cluster structure |
| DBSCAN | Arbitrary-shaped clusters + need noise/outlier detection |
| Gaussian Mixture Model | Soft/probabilistic cluster assignment |
| Mean Shift | Don't want to specify k in advance |
| Spectral Clustering | Graph-structured similarity, non-convex clusters |

## Ensemble techniques

| Technique | Mechanism | Examples |
|---|---|---|
| Bagging | Train many models in parallel on bootstrapped samples, average | Random Forest |
| Boosting | Train sequentially, each model corrects prior errors | AdaBoost, XGBoost, LightGBM, CatBoost, Gradient Boosting |
| Stacking | Train a meta-model on the outputs of base models | Stacking ensembles |

## Reinforcement learning

| Category | Algorithms | Use case |
|---|---|---|
| Value-based | Q-Learning, Deep Q-Network (DQN), SARSA | Discrete action spaces, learn a value function |
| Policy/Actor-Critic | A3C | Continuous or complex action spaces |

## Dimensionality reduction

| Technique | Type | Use case |
|---|---|---|
| PCA | Linear | General-purpose variance-preserving reduction |
| LDA | Linear | Reduction that also separates known classes |
| SVD | Linear | Recommender systems, PCA under the hood |
| t-SNE | Non-linear | Visualization (2D/3D), NOT for downstream modeling |
| UMAP / LLE | Non-linear | Visualization + some downstream use |
| ICA | Linear | Separating mixed signals (e.g., audio source separation) |

## Quick selection guide

| Problem | Recommended |
|---|---|
| Predict a price/continuous value | Linear Regression → Random Forest → XGBoost (in order of complexity) |
| Predict a category | Logistic Regression → Random Forest → Gradient Boosting |
| Find customer segments | K-Means (if roughly spherical) or DBSCAN (if irregular shapes + outliers) |
| High-dimensional data, need fewer features | PCA (for modeling) or t-SNE/UMAP (for visualization only) |
| Automatic feature selection | Lasso, or feature importances from Random Forest/XGBoost |
| Best possible tabular accuracy, have time to tune | XGBoost / LightGBM / CatBoost |
| Need to explain the decision to a non-technical stakeholder | Single Decision Tree or Logistic Regression, not an ensemble |
