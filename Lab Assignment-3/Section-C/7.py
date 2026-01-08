# 7. Plot multiple lines in a single figure representing sales across 3 years.
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales_2021 = [50, 60, 55, 65, 70]
sales_2022 = [55, 62, 58, 68, 75]
sales_2023 = [60, 65, 63, 70, 80]
plt.plot(months, sales_2021, marker='o', label="2021")
plt.plot(months, sales_2022, marker='o', label="2022")
plt.plot(months, sales_2023, marker='o', label="2023")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Comparison Across 3 Years")
plt.legend()
plt.show()
print("Shomya Sarraf,23053668")