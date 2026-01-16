#  7. Effect of Learning Rate
# Train logistic regression with different learning rates and compare:
# A. Speed of convergence
# B. Stability of loss
import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4, 5])
y = np.array([0, 0, 0, 1, 1])
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def log_loss(y, y_pred):
    return -np.mean(y*np.log(y_pred) + (1-y)*np.log(1-y_pred))
learning_rates = [0.01, 0.1, 1.0]
plt.figure(figsize=(8,6))
for lr in learning_rates:
    w, b = 0.0, 0.0
    losses = []
    for i in range(100):
        z = w*X + b
        y_pred = sigmoid(z)
        loss = log_loss(y, y_pred)
        losses.append(loss)
        dw = np.mean((y_pred - y) * X)
        db = np.mean(y_pred - y)
        w -= lr * dw
        b -= lr * db
    plt.plot(losses, label=f"lr = {lr}")
plt.xlabel("Iterations")
plt.ylabel("Log Loss")
plt.title("Effect of Learning Rate on Convergence")
plt.legend()
plt.show()
print("Shomya Sarraf , 23053668")
