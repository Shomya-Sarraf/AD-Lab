# 1. Binary Classification Using Logistic Regression
# Write a Python program to implement Logistic Regression from scratch (without using sklearn) for a binary classification dataset with one feature. Plot the sigmoid curve.
import numpy as np
import matplotlib.pyplot as plt
X = np.array([1,2,3,4,5])
y = np.array([0,0,0,1,1])
def sigmoid(z):
    return 1/(1+np.exp(-z))
w, b = 0, 0
lr = 0.1
for i in range(1000):
    z = w*X + b
    y_pred = sigmoid(z)
    w -= lr * np.mean((y_pred - y) * X)
    b -= lr * np.mean(y_pred - y)
x_vals = np.linspace(0,6,100)
plt.plot(x_vals, sigmoid(w*x_vals + b))
plt.scatter(X, y)
plt.show()
print("Shomya Sarraf , 23053668")
