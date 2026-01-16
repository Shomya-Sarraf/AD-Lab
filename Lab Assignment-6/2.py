# 2. Implement Gaussian Naïve Bayes without using any ML
#  library.Compute mean, variance, and posterior probability manually.
import math
X = [[1,20],[2,21],[3,22],[8,30],[9,31],[10,32]]
y = [0,0,0,1,1,1]
def mean(values):
    return sum(values)/len(values)
def variance(values, m):
    return sum((x-m)**2 for x in values)/len(values)
def gaussian(x, m, v):
    return (1/math.sqrt(2*math.pi*v)) * math.exp(-(x-m)**2/(2*v))
stats = {}
for c in [0,1]:
    xs = [X[i] for i in range(len(X)) if y[i]==c]
    stats[c] = []
    for j in range(len(X[0])):
        col = [row[j] for row in xs]
        stats[c].append((mean(col), variance(col, mean(col))))
print(stats)
print("Shomya Sarraf, 23053668")