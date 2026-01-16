# 17. Perfect Separation Case
# Create a perfectly separable dataset and observe what happens to coefficients during training.
import numpy as np
from sklearn.linear_model import LogisticRegression
X = np.array([
    [1], [2], [3], [4],      # Class 0
    [10], [11], [12], [13]  # Class 1
])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
model = LogisticRegression(max_iter=1000)
model.fit(X, y)
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Shomya Sarraf , 23053668")
