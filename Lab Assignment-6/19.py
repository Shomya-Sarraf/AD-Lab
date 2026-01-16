# 19. Compare Gaussian NB vs Logistic Regression on the same dataset
# and analyze results.
import math
X = [
    [1, 1], [2, 2], [3, 3], [4, 4],     
    [7, 7], [8, 8], [9, 9], [10, 10]   
]
y = [0, 0, 0, 0, 1, 1, 1, 1]
def mean(values):
    return sum(values) / len(values)
def variance(values, m):
    return sum((x - m) ** 2 for x in values) / len(values)
def gaussian(x, m, v):
    return (1 / math.sqrt(2 * math.pi * v)) * math.exp(-(x - m) ** 2 / (2 * v))
stats = {}
for c in [0, 1]:
    class_data = [X[i] for i in range(len(X)) if y[i] == c]
    stats[c] = []
    for j in range(2):
        col = [row[j] for row in class_data]
        stats[c].append((mean(col), variance(col, mean(col))))
def predict_nb(point):
    probs = {}
    for c in stats:
        probs[c] = 1
        for i in range(2):
            m, v = stats[c][i]
            probs[c] *= gaussian(point[i], m, v)
    return max(probs, key=probs.get)
w1, w2, b = 0.5, 0.5, -5
def sigmoid(z):
    return 1 / (1 + math.exp(-z))
def predict_lr(point):
    z = w1*point[0] + w2*point[1] + b
    return 1 if sigmoid(z) >= 0.5 else 0
print("Point | Naïve Bayes | Logistic Regression")
for i in range(len(X)):
    nb = predict_nb(X[i])
    lr = predict_lr(X[i])
    print(X[i], " | ", nb, " | ", lr)
print("Shomya Sarraf, 23053668")
