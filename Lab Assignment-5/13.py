# 13. Medical Diagnosis Prediction
# Use logistic regression to predict disease presence based on medical features. Interpret coefficients in terms of odds ratio.
import numpy as np
from sklearn.linear_model import LogisticRegression
X = np.array([
    [1, 140, 180],
    [0, 120, 100],
    [1, 150, 200],
    [0, 110, 90],
    [1, 160, 210]
])
y = np.array([1, 0, 1, 0, 1])
model = LogisticRegression()
model.fit(X, y)
coefficients = model.coef_[0]
intercept = model.intercept_[0]
odds_ratios = np.exp(coefficients)
print("Coefficients:", coefficients)
print("Intercept:", intercept)
print("Odds Ratios:", odds_ratios)
new_patient = np.array([[1, 145, 190]])
prediction = model.predict(new_patient)
probability = model.predict_proba(new_patient)
print("\nPrediction (1 = Disease, 0 = No Disease):", prediction)
print("Disease Probability:", probability)
print("Shomya Sarraf , 23053668")
