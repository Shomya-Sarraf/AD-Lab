# 12. Detect outliers in a numeric column using IQR method.
import pandas as pd
data = pd.DataFrame({"value": [10, 12, 11, 200, 13]})
Q1 = data["value"].quantile(0.25)
Q3 = data["value"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(data[(data["value"] < lower) | (data["value"] > upper)])
print("Shomya Sarraf,23053668")