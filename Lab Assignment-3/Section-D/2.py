# 2. Standardize a numeric column (z-score normalization).
import pandas as pd
data = pd.Series([10, 20, 30, 40, 50])
mean = data.mean()
std = data.std()
z_scores = (data - mean) / std
print(z_scores)
print("Shomya Sarraf,23053668")
