# 2. Write a program to calculate Entropy for a given class distribution.
import numpy as np
def entropy(y):
    values, counts = np.unique(y, return_counts=True)
    prob = counts / counts.sum()
    return -np.sum(prob * np.log2(prob))
y = np.array([1, 1, 1, 0, 0])
print("Entropy:", entropy(y))
print("Shomya Sarraf , 23053668")
