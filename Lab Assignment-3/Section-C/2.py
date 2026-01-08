# 2. Create a bar chart comparing average marks of 5 students.
import matplotlib.pyplot as plt
students = ["A", "B", "C", "D", "E"]
marks = [78, 85, 67, 90, 72]
plt.bar(students, marks, color='skyblue')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Average Marks of Students")
plt.show()
print("Shomya Sarraf,23053668")