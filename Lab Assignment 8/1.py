# 1. Manual PCA from Scratch
# Write a Python program to:
# A. Standardize a dataset
# B. Compute covariance matrix
# C. Calculate eigenvalues and eigenvectors
# D. Sort eigenvalues in descending order
# E. Project data onto first two principal components

import numpy as np
from sklearn.datasets import load_iris
# Load data
X = load_iris().data
# A. Standardize
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_stdized = (X - X_mean) / X_std
# B. Covariance matrix
cov_matrix = np.cov(X_stdized.T)
# C. Eigenvalues & eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
# D. Sort eigenvalues (descending)
sorted_idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_idx]
eigenvectors = eigenvectors[:, sorted_idx]
# E. Project onto first 2 PCs
W = eigenvectors[:, :2]
X_pca = X_stdized @ W
print("Eigenvalues:", eigenvalues)
print("Projected shape:", X_pca.shape)
print("Shomya Sarraf, 23053668")
