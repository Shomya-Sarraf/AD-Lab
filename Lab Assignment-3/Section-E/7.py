# 7. Implement a polynomial regression (degree 2) and plot predicted curve.
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 55, 65, 80, 110])
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)
# Plot
plt.scatter(X, y)
plt.plot(X, model.predict(X_poly))
plt.title("Polynomial Regression (Degree 2)")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()
print("Shomya Sarraf,23053668")