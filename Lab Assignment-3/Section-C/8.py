# 8. Plot pie chart showing percentage distribution of different categories.
import matplotlib.pyplot as plt
categories = ["Electronics", "Clothes", "Grocery", "Toys"]
values = [40, 25, 20, 15]
plt.pie(values, labels=categories, autopct="%0.1f%%")
plt.title("Category Distribution")
plt.show()
print("Shomya Sarraf,23053668")
