# 1. Train a Linear Regression model to predict house prices using one feature.
from sklearn.linear_model import LinearRegression
import numpy as np
# X = size of house, y = price
X = np.array([[500], [1000], [1500], [2000]])
y = np.array([50, 100, 150, 200])   # price in lakhs
model = LinearRegression()
model.fit(X, y)
print("Prediction for 1200 sq.ft =", model.predict([[1200]]))
print("Slope (coef):", model.coef_)
print("Intercept:", model.intercept_)
print("Shomya Sarraf,23053668")