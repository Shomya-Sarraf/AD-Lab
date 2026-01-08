# 14. Save cleaned data into a new CSV file.
import pandas as pd
import numpy as np
data = pd.DataFrame({
    "A": [1, np.nan, 3],
    "B": ["x", None, "y"]
})
data["A"] = data["A"].fillna(data["A"].mean())
data["B"] = data["B"].fillna(data["B"].mode()[0])
data.to_csv("cleaned.csv", index=False)
print("Saved cleaned.csv")
print("Shomya Sarraf,23053668")
