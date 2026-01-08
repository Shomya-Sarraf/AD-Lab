# 2. Fit a Multiple Linear Regression model and evaluate R² score.
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
X = np.array([
    [500, 1],
    [1000, 2],
    [1500, 3],
    [2000, 4]
])
y = np.array([50, 100, 150, 200])  # price
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print("R² Score:", r2_score(y, y_pred))
print("Shomya Sarraf,23053668")
