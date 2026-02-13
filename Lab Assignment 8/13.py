# 13. PCA and Explained Variance Threshold
# Write a function that:
# A. Automatically selects number of components
# B. Based on variance threshold (e.g., 90%)

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import numpy as np
def pca_auto(X, threshold=0.90):
    pca = PCA()
    pca.fit(X)
    cum_var = np.cumsum(pca.explained_variance_ratio_)
    k = np.argmax(cum_var >= threshold) + 1
    return PCA(n_components=k).fit_transform(X), k
X = load_iris().data
X_new, k = pca_auto(X, 0.9)
print("Selected components:", k)
print("Shomya Sarraf, 23053668")