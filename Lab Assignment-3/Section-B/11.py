# 11. Create a pivot table from a DataFrame.
import pandas as pd
data = pd.DataFrame({
    "region": ["East", "East", "West"],
    "product": ["A", "B", "A"],
    "sales": [100, 200, 150]
})
pivot = data.pivot_table(values="sales", index="region", columns="product", aggfunc="sum")
print(pivot)
print("Shomya Sarraf,23053668")
