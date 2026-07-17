# Neural Network Architectures & Backpropagation

## 25 architectures at a glance

| # | Architecture | Core idea | Best for |
|---|---|---|---|
| 1 | Feedforward (FNN/MLP) | Info flows input→output, no loops | Tabular baseline |
| 2 | CNN | Convolutional filters detect local spatial patterns | Images |
| 3 | RNN | Loops carry memory across a sequence | Sequences (short) |
| 4 | LSTM | Gated RNN — input/forget/output gates | Long-range sequence dependencies |
| 5 | GRU | Simplified LSTM (update/reset gates) | Sequences, faster than LSTM |
| 6 | Bidirectional RNN | Processes sequence forward + backward | Full-context NLP |
| 7 | Deep Belief Network | Stacked Restricted Boltzmann Machines | Representation learning (largely historical) |
| 8 | Autoencoder | Compress then reconstruct input | Compression, denoising, anomaly detection |
| 9 | Variational Autoencoder (VAE) | Probabilistic autoencoder | Generative modeling |
| 10 | GAN | Generator vs Discriminator adversarial training | Image/data generation |
| 11 | Transformer | Self-attention across full sequence, parallelizable | Foundation models, translation, generation |
| 12 | Vision Transformer (ViT) | Transformer applied to image patches | Image classification at scale |
| 13 | Graph Neural Network (GNN) | Learns over graph-structured data | Node/edge/graph prediction |
| 14 | Graph Attention Network (GAT) | Attention-weighted neighbor aggregation | Graph learning w/ variable neighbor importance |
| 15 | Message Passing NN (MPNN) | General graph framework, aggregates neighbor info | Molecular prediction |
| 16 | Capsule Network | Preserves spatial hierarchies via "capsules" | Pose-aware image recognition |
| 17 | ResNet | Skip connections | Very deep CNNs without vanishing gradients |
| 18 | DenseNet | Every layer connects to every other layer | Feature reuse, parameter efficiency |
| 19 | Inception | Parallel multi-scale convolutions (1x1, 3x3, 5x5, pool) | Multi-scale image features |
| 20 | U-Net | Encoder-decoder with skip connections | Image segmentation (esp. medical) |
| 21 | Siamese Network | Shared weights, compares two inputs | Face verification, similarity |
| 22 | Triplet Network | Anchor/positive/negative triplet loss | Metric/embedding learning |
| 23 | Neural ODE | Continuous-depth net via differential equations | Continuous-time modeling |
| 24 | Spiking Neural Network (SNN) | Discrete spikes, biologically inspired | Neuromorphic hardware, low power |
| 25 | Diffusion Model | Iteratively denoises random noise into data | State-of-the-art image generation |

## Quick selection guide

| Data type | Architecture |
|---|---|
| Tabular | MLP/FNN |
| Images (classification) | CNN, ResNet, ViT |
| Images (segmentation) | U-Net |
| Sequences (short) | RNN |
| Sequences (long-range) | LSTM, GRU, Transformer |
| Text/language | Transformer (BERT-style encoder, GPT-style decoder) |
| Graph data | GNN, GAT, MPNN |
| Generate new data | GAN, VAE, Diffusion Model |
| Similarity/verification | Siamese, Triplet Network |
| Low-power/edge hardware | SNN |

## Backpropagation — the mechanics

**Forward pass:** compute ŷ from x using weights W and biases b through each layer.
**Loss:** L(ŷ, y) — e.g., MSE for regression, cross-entropy for classification.
**Backward pass:** propagate the error gradient from output layer back through hidden layers via the chain rule.

Key equations:
- Output layer error: δ(L) = ∂L/∂a(L) ⊙ f'(z(L))
- For MSE + sigmoid: δ(L) = (a(L) − y) ⊙ f'(z(L))
- Hidden layer error: δ(l) = (W(l+1))ᵀδ(l+1) ⊙ f'(z(l))
- Weight gradient: ∂L/∂W(l) = δ(l)(a(l−1))ᵀ
- Bias gradient: ∂L/∂b(l) = Σδ(l) (summed over the mini-batch)

Minimal Python (2-2-1 network, sigmoid, MSE):
```python
import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

x = np.array([[0.5, 0.1]])
y_true = np.array([[1.0]])

# forward
z1 = np.dot(x, w1) + b1
a1 = sigmoid(z1)
z2 = np.dot(a1, w2) + b2
a2 = sigmoid(z2)
loss = np.mean((a2 - y_true) ** 2)

# backward
m = y_true.shape[0]
dz2 = (2/m) * (a2 - y_true) * sigmoid_derivative(z2)
dw2 = np.dot(a1.T, dz2)
db2 = np.sum(dz2, axis=0, keepdims=True)
dz1 = np.dot(dz2, w2.T) * sigmoid_derivative(z1)
dw1 = np.dot(x.T, dz1)
db1 = np.sum(dz1, axis=0, keepdims=True)
```

**Key takeaway:** backprop efficiently computes gradients by propagating the error from the output layer backward, then gradient descent uses those gradients to update weights and reduce loss.
