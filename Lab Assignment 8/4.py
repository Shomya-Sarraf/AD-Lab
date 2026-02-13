# 4. Effect of Feature Scaling
# Apply PCA:
# A. Without scaling
# B. After StandardScaler
# Compare:
# A. Eigenvalues
# B. Principal components
# C. Explained variance

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
X = load_iris().data
# Without scaling
pca1 = PCA().fit(X)
# With scaling
X_scaled = StandardScaler().fit_transform(X)
pca2 = PCA().fit(X_scaled)
print("Eigenvalues without scaling:", pca1.explained_variance_)
print("Eigenvalues with scaling:", pca2.explained_variance_)
print("Shomya Sarraf, 23053668")