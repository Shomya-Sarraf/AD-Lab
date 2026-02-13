# 2. PCA Using scikit-learn
# Load the Iris dataset and:
# A. Apply PCA
# B. Reduce to 2 components
# C. Display explained variance ratio
# D. Visualize transformed data

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
X = iris.data
y = iris.target
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("Explained variance ratio:", pca.explained_variance_ratio_)
plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.title("PCA - Iris")
plt.show()
print("Shomya Sarraf, 23053668")