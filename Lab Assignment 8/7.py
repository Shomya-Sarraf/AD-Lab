# 7. PCA on High-Dimensional Data
# Generate synthetic dataset with 100 features:
# A. Apply PCA
# B. Plot eigenvalue spectrum
# C. Identify intrinsic dimensionality

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
X = np.random.rand(100, 100)  # 100 samples, 100 features
pca = PCA()
pca.fit(X)
plt.plot(pca.explained_variance_)
plt.title("Eigenvalue Spectrum")
plt.show()
print("Shomya Sarraf, 23053668")