# 8. Feature Scaling Impact
# Train logistic regression:
# A. With unscaled features
# B. With standardized features
# C. Compare convergence speed and accuracy.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    random_state=42
)
model_unscaled = LogisticRegression(max_iter=100)
model_unscaled.fit(X, y)
y_pred_unscaled = model_unscaled.predict(X)
acc_unscaled = accuracy_score(y, y_pred_unscaled)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model_scaled = LogisticRegression(max_iter=100)
model_scaled.fit(X_scaled, y)
y_pred_scaled = model_scaled.predict(X_scaled)
acc_scaled = accuracy_score(y, y_pred_scaled)
print("Accuracy without scaling:", acc_unscaled)
print("Accuracy with scaling:", acc_scaled)
print("Iterations without scaling:", model_unscaled.n_iter_)
print("Iterations with scaling:", model_scaled.n_iter_)
print("Shomya Sarraf , 23053668")
