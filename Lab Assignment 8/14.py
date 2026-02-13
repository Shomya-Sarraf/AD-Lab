# 14. PCA Using SVD
# Implement PCA using Singular Value Decomposition (SVD) instead of eigen
# decomposition and compare results.

import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
X = load_iris().data
X = (X - X.mean(axis=0)) / X.std(axis=0)
U, S, VT = np.linalg.svd(X, full_matrices=False)
W_svd = VT.T[:, :2]
X_pca_svd = X @ W_svd
pca = PCA(n_components=2)
X_pca_sklearn = pca.fit_transform(X)
print("SVD PCA shape:", X_pca_svd.shape)
print("Sklearn PCA shape:", X_pca_sklearn.shape)
print("Shomya Sarraf, 23053668")