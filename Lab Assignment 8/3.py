# 3. Cumulative Variance Plot
# Write a program to:
# A. Compute cumulative explained variance
# B. Plot variance vs number of components
# C. Determine minimum components to retain 95% variance

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
X = load_iris().data
pca = PCA()
pca.fit(X)
cum_var = np.cumsum(pca.explained_variance_ratio_)
plt.plot(cum_var, marker='o')
plt.axhline(y=0.95, linestyle='--')
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Variance")
plt.show()
# Minimum components for 95%
k = np.argmax(cum_var >= 0.95) + 1
print("Components for 95% variance:", k)
print("Shomya Sarraf, 23053668")