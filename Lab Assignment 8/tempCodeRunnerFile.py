import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()
img = digits.data[0].reshape(8,8)
pca = PCA(n_components=10)
compressed = pca.fit_transform(img)
reconstructed = pca.inverse_transform(compressed)
plt.imshow(reconstructed, cmap='gray')
plt.show()
print("Shomya Sarraf, 23053668")