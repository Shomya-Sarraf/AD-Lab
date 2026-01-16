# 12. Write code to demonstrate how Naïve Bayes behaves when features
# are strongly correlated.
import math
X = [
    [1, 1], [2, 2], [3, 3], [4, 4],
    [8, 8], [9, 9], [10, 10], [11, 11]
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
    for j in range(len(X[0])):
        column = [row[j] for row in class_data]
        m = mean(column)
        v = variance(column, m)
        stats[c].append((m, v))
def predict(x):
    probs = {}
    for c in stats:
        probs[c] = 1
        for i in range(len(x)):
            m, v = stats[c][i]
            probs[c] *= gaussian(x[i], m, v)
    return max(probs, key=probs.get)
test_point = [3, 3]
result = predict(test_point)
print("Test point:", test_point)
print("Predicted class:", result)
print("Shomya Sarraf, 23053668")
