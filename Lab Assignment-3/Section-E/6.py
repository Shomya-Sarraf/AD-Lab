# 6. Train a K-Means clustering algorithm with K=3 and show cluster centroids.
from sklearn.cluster import KMeans
import numpy as np
data = np.array([
    [1,2], [1,3], [2,2],
    [8,8], [8,9], [9,8],
    [4,10], [5,10], [4,11]
])
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
print("Cluster centers:\n",kmeans.cluster_centers_)
print("Labels:",kmeans.labels_)
print("Shomya Sarraf,23053668")