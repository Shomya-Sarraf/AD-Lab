# 20. Explainability of Logistic Regression
# Compute odds ratio and interpret feature importance in real-world terms.
import numpy as np
from sklearn.linear_model import LogisticRegression
X = np.array([
    [2, 60, 5],
    [4, 70, 6],
    [6, 80, 7],
    [8, 90, 8],
    [1, 50, 4],
    [7, 85, 7]
])
y = np.array([0, 0, 1, 1, 0, 1])
model = LogisticRegression()
model.fit(X, y)
coefficients = model.coef_[0]
intercept = model.intercept_[0]
odds_ratios = np.exp(coefficients)
print("Coefficients:", coefficients)
print("Odds Ratios:", odds_ratios)
print("Intercept:", intercept)
print("Shomya Sarraf , 23053668")
