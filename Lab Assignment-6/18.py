# 18. Write a program to visualize decision boundaries of Naïve Bayes for a
# 2-feature dataset.
import math
import matplotlib.pyplot as plt
X = [
    [1, 1], [2, 2], [3, 3], [4, 4],     # Class 0
    [7, 7], [8, 8], [9, 9], [10, 10]    # Class 1
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
        column = [row[j] for row in class_data]
        m = mean(column)
        v = variance(column, m)
        stats[c].append((m, v))
def predict(point):
    probs = {}
    for c in stats:
        probs[c] = 1
        for i in range(2):
            m, v = stats[c][i]
            probs[c] *= gaussian(point[i], m, v)
    return max(probs, key=probs.get)
xx = []
yy = []
cc = []
for i in range(0, 120):
    for j in range(0, 120):
        p = [i/10, j/10]
        cls = predict(p)
        xx.append(p[0])
        yy.append(p[1])
        cc.append(cls)
for i in range(len(X)):
    if y[i] == 0:
        plt.scatter(X[i][0], X[i][1], color="blue")
    else:
        plt.scatter(X[i][0], X[i][1], color="red")
plt.scatter(xx, yy, c=cc, alpha=0.1)
plt.title("Naïve Bayes Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
print("Shomya Sarraf, 23053668")