# 14. Student Pass/Fail Prediction
# Build a logistic regression model to predict pass/fail using attendance and marks. Explain decision boundary
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
X = np.array([
    [60, 40],
    [70, 45],
    [80, 60],
    [90, 75],
    [50, 30],
    [85, 70],
    [40, 20],
    [75, 55]
])
y = np.array([0, 0, 1, 1, 0, 1, 0, 1])
model = LogisticRegression()
model.fit(X, y)
w1, w2 = model.coef_[0]
b = model.intercept_[0]
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm')
x_vals = np.linspace(40, 95, 100)
y_vals = -(w1 * x_vals + b) / w2
plt.plot(x_vals, y_vals, color='black')
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.title("Student Pass/Fail Decision Boundary")
plt.show()
print("Shomya Sarraf , 23053668")
