# 11. PCA and Correlated Features
# Generate correlated features:
# A. Apply PCA
# B. Observe dimensionality reduction
# C. Explain eigenvalue distribution

import numpy as np
from sklearn.decomposition import PCA
x = np.random.rand(100)
y = x * 0.9 + np.random.rand(100)*0.1
X = np.vstack([x, y]).T
pca = PCA().fit(X)
print("Eigenvalues:", pca.explained_variance_)
print("Shomya Sarraf, 23053668")