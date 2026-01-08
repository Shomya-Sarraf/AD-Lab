# 5. Filter rows using multiple conditions (AND / OR operations).
import pandas as pd
data = pd.DataFrame({
    "age": [20, 30, 40],
    "score": [50, 80, 70]
})
print("AND:\n", data[(data["age"] > 25) & (data["score"] > 60)])
print("OR:\n", data[(data["age"] < 25) | (data["score"] >= 80)])
print("Shomya Sarraf,23053668")
