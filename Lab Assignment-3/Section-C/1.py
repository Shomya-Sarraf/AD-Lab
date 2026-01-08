# 1. Plot a line graph showing population growth across years.
import matplotlib.pyplot as plt
years = [2000, 2005, 2010, 2015, 2020]
population = [50, 55, 60, 70, 80]
plt.plot(years, population, marker='o')
plt.xlabel("Year")
plt.ylabel("Population (in millions)")
plt.title("Population Growth")
plt.show()
print("Shomya Sarraf,23053668")