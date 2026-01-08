# 8. Convert a skewed column using log-transformation and analyze improvement
import pandas as pd
import numpy as np
data = pd.Series([10, 20, 30, 1000, 2000, 5000])   # skewed data
print("Before log transformation:")
print(data)
log_data = np.log(data) # Apply log transform
print("\nAfter log transformation:")
print(log_data)
print("Shomya Sarraf,23053668")
