# 9. PCA for Image Compression
# Load a grayscale image:
# A. Apply PCA
# B. Reconstruct image using different k values
# C. Compare reconstruction quality

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
X = digits.data  # shape (1797, 64)

# Apply PCA
pca = PCA(n_components=10)
X_compressed = pca.fit_transform(X)

# Reconstruct first image
X_reconstructed = pca.inverse_transform(X_compressed)

img_reconstructed = X_reconstructed[0].reshape(8,8)

plt.imshow(img_reconstructed, cmap='gray')
plt.title("Reconstructed Image (k=10)")
plt.show()

print("Shomya Sarraf, 23053668")
