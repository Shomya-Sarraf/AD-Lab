# 10. Compare PCA and Random Projection
# Reduce dimensionality using:
# A. PCA
# B. Random Projection
# Compare:
# A. Classification accuracy
# B. Variance retained

from sklearn.random_projection import GaussianRandomProjection
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
rp = GaussianRandomProjection(n_components=2)
X_rp = rp.fit_transform(X)
print("PCA variance:", sum(pca.explained_variance_ratio_))
print("Shomya Sarraf, 23053668")