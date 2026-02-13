# 6. PCA for Noise Reduction
# Add Gaussian noise to a dataset:
# A. Apply PCA
# B. Reconstruct dataset using top k components
# C. Compute reconstruction MSE

import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error
X = load_iris().data
noise = np.random.normal(0, 0.5, X.shape)
X_noisy = X + noise
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_noisy)
X_reconstructed = pca.inverse_transform(X_reduced)
mse = mean_squared_error(X, X_reconstructed)
print("Reconstruction MSE:", mse)
print("Shomya Sarraf, 23053668")