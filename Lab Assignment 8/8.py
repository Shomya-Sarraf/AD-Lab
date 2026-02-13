# 8. Visualization of Principal Directions
# For 2D synthetic dataset:
# A. Plot original data
# B. Plot principal component vectors
# C. Show projection onto first PC

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
# synthetic data
X = np.random.randn(200,2)
X[:,1] = X[:,0]*0.8 + np.random.randn(200)*0.1
pca = PCA(n_components=2)
pca.fit(X)
plt.scatter(X[:,0], X[:,1])
for vec in pca.components_:
    plt.quiver(0,0, vec[0], vec[1], scale=2)
plt.show()
print("Shomya Sarraf, 23053668")