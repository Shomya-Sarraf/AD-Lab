# 3. Sigmoid Function Implementation
# Write a program to:
# A. Implement the sigmoid function
# B. Plot sigmoid for values from −10 to +10
# C. Explain its role in logistic regression
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = 1/(1+np.exp(-x))
plt.plot(x, y)
plt.show()
print("Shomya Sarraf , 23053668")
