# Math Foundations for Data Science

24 formulas that show up constantly across ML, stats, and optimization. Grouped by function, not source order.

## Optimization

| Concept | Formula | Terms | Used for |
|---|---|---|---|
| **Gradient Descent** | θ(j+1) = θj − α·∇J(θj) | θ: parameters, α: learning rate, ∇J: gradient of loss | Training any model with a differentiable loss |
| **Lagrange Multiplier** | L(x,λ) = f(x) − λ·g(x), solving max f(x) s.t. g(x)=0 | λ: multiplier | Constrained optimization |
| **SVM objective** | min(w,b) ½‖w‖² + C·Σ max(0, 1 − yᵢ(w·xᵢ − b)) | C: penalty for margin violation | Max-margin classification/regression |

## Probability & Statistics Building Blocks

| Concept | Formula | Terms | Used for |
|---|---|---|---|
| **Normal Distribution** | f(x\|μ,σ²) = (1/(σ√(2π)))·exp(−(x−μ)²/(2σ²)) | μ: mean, σ: std dev | Statistical modeling, hypothesis testing |
| **Z-Score** | z = (x−μ)/σ | | Normalization, outlier detection |
| **Correlation** | Corr(X,Y) = Cov(X,Y)/(Std(X)·Std(Y)) | range −1 to 1 | Relationship strength between two variables |
| **MLE** | argmax(θ) Π P(xᵢ\|θ) | | Parameter estimation |
| **Entropy** | H(S) = −Σ pᵢ·log₂(pᵢ) | | Decision trees, information theory |
| **KL Divergence** | D_KL(P‖Q) = Σ P(x)·log(P(x)/Q(x)) | P: true dist, Q: predicted dist | Compare distributions (VAEs, distillation) |

## Regression & Fit

| Concept | Formula | Terms | Used for |
|---|---|---|---|
| **OLS** | β = (XᵀX)⁻¹XᵀY | | Closed-form linear regression |
| **Linear Regression** | y = β0 + β1x1 + ... + βnxn + ε | ε: error term | Continuous prediction |
| **MSE** | (1/n)Σ(yᵢ−ŷᵢ)² | | Regression loss |
| **MSE + L2 (Ridge)** | MSE + λΣβj² | λ: regularization strength | Prevent overfitting, shrink coefficients |
| **R² Score** | 1 − [Σ(yᵢ−ŷᵢ)² / Σ(yᵢ−ȳ)²] | | % variance explained by the model |

## Classification & Activation

| Concept | Formula | Terms | Used for |
|---|---|---|---|
| **Sigmoid** | σ(x) = 1/(1+e^(−x)) | | Binary classification, logistic regression, NN activation |
| **Softmax** | P(y=j\|x) = e^(xᵀwj) / Σ e^(xᵀwk) | | Multi-class output probabilities |
| **ReLU** | ReLU(x) = max(0, x) | | Default hidden-layer activation in deep nets |
| **Naive Bayes** | P(y\|x1..xn) = P(y)·Π P(xᵢ\|y) / P(x1..xn) | assumes feature independence | Text classification, spam filters |
| **Log Loss** | −(1/N)Σ[yᵢlog(ŷᵢ) + (1−yᵢ)log(1−ŷᵢ)] | | Binary classification loss |
| **F1 Score** | F1 = 2·P·R / (P+R) | P: precision, R: recall | Classification eval, esp. imbalanced classes |

## Similarity & Dimensionality

| Concept | Formula | Terms | Used for |
|---|---|---|---|
| **Cosine Similarity** | similarity = (A·B)/(‖A‖·‖B‖) | | Vector/embedding similarity, recommendation, semantic search |
| **SVD** | A = UΣVᵀ | | Dimensionality reduction, PCA, recommender systems |
| **Eigenvectors** | Av = λv | A: matrix, v: eigenvector, λ: eigenvalue | PCA, feature extraction |
| **K-Means objective** | J = Σᵢ Σ(x∈Sᵢ) ‖x−μᵢ‖² | μᵢ: cluster centroid | Clustering, minimizing within-cluster variance |

## Quick lookup by task

| Task | Reach for |
|---|---|
| "Why is my model's loss not decreasing" | Gradient Descent, learning rate α |
| "Is this variable normal-ish" | Z-Score, Normal Distribution |
| "How similar are these two documents/embeddings" | Cosine Similarity |
| "Reduce 500 features to 20" | SVD / Eigenvectors (PCA) |
| "My linear model overfits" | MSE + L2 (Ridge) |
| "Evaluate an imbalanced classifier" | F1 Score, not raw accuracy |
| "Compare two probability distributions" | KL Divergence |
