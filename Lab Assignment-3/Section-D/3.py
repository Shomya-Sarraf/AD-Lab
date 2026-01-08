# 3. Apply min-max normalization on a dataset column.
import pandas as pd
data = pd.Series([5, 10, 15, 20, 25])
min_val = data.min()
max_val = data.max()
normalized = (data - min_val) / (max_val - min_val)
print(normalized)
print("Shomya Sarraf,23053668")
