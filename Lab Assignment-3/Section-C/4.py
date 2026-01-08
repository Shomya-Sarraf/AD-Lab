# 4. Create a scatter plot between “salary” and “experience”.
import matplotlib.pyplot as plt
experience = [1, 2, 3, 4, 5, 6, 7]
salary = [25000, 30000, 35000, 40000, 50000, 60000, 70000]
plt.scatter(experience, salary, color='red')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.show()
print("Shomya Sarraf,23053668")