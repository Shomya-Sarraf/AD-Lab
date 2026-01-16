#  6. Gradient Descent for Logistic Regression
# Implement logistic regression using gradient descent and:
# A. Plot loss vs iterations
# B. Analyze convergence
import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4, 5])
y = np.array([0, 0, 0, 1, 1])
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def log_loss(y, y_pred):
    return -np.mean(y*np.log(y_pred) + (1-y)*np.log(1-y_pred))
w = 0.0
b = 0.0
lr = 0.1
iterations = 100
losses = []
for i in range(iterations):
    z = w*X + b
    y_pred = sigmoid(z)
    loss = log_loss(y, y_pred)
    losses.append(loss)
    dw = np.mean((y_pred - y) * X)
    db = np.mean(y_pred - y)
    w -= lr * dw
    b -= lr * db
plt.plot(range(iterations), losses)
plt.xlabel("Iterations")
plt.ylabel("Log Loss")
plt.title("Loss vs Iterations")
plt.show()
print("Final Weight:", w)
print("Final Bias:", b)
print("Shomya Sarraf , 23053668")
