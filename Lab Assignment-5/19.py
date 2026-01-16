#  19. Compare Logistic vs Linear Regression
# Use linear regression and logistic regression on a binary dataset and compare predictions.
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 0, 1, 1])   
lin_model = LinearRegression()
lin_model.fit(X, y)
lin_pred = lin_model.predict(X)
log_model = LogisticRegression()
log_model.fit(X, y)
log_pred = log_model.predict(X)
log_prob = log_model.predict_proba(X)
print("Linear Regression Predictions:")
print(lin_pred)
print("\nLogistic Regression Class Predictions:")
print(log_pred)
print("\nLogistic Regression Probabilities:")
print(log_prob)
print("Shomya Sarraf , 23053668")
