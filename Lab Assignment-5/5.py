# 5. Log-Loss Calculation
# Given predicted probabilities and true labels, compute log-loss manually and verify with sklearn.
import numpy as np
from sklearn.metrics import log_loss
y_true = np.array([1, 0, 1, 1, 0])
y_pred = np.array([0.9, 0.2, 0.8, 0.7, 0.1])
manual_loss = -np.mean(
    y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)
)
print("Manual Log-Loss:", manual_loss)
sklearn_loss = log_loss(y_true, y_pred)
print("Sklearn Log-Loss:", sklearn_loss)
print("Shomya Sarraf , 23053668")
