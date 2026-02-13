# 15. PCA Reconstruction Error Analysis
# For different values of k:
# A. Project data
# B. Reconstruct data
# C. Plot reconstruction error vs k
# D. Interpret bias–variance tradeoff

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
X = load_iris().data
X = (X - X.mean(axis=0)) / X.std(axis=0)
errors = []
components = range(1, X.shape[1] + 1)
for k in components:
    pca = PCA(n_components=k)
    X_reduced = pca.fit_transform(X)
    X_reconstructed = pca.inverse_transform(X_reduced)
    mse = mean_squared_error(X, X_reconstructed)
    errors.append(mse)
plt.plot(components, errors, marker='o')
plt.xlabel("Number of Components (k)")
plt.ylabel("Reconstruction Error (MSE)")
plt.title("PCA Reconstruction Error")
plt.show()
print("Shomya Sarraf, 23053668")