# 3. Plot a histogram for the age distribution from a dataset.
import matplotlib.pyplot as plt
ages = [18, 19, 22, 25, 30, 35, 40, 22, 25, 27, 29, 30, 40, 45]
plt.hist(ages, bins=5, color='orange')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()
print("Shomya Sarraf,23053668")