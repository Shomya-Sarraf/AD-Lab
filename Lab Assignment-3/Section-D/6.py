# 6. Compute correlation coefficient between two numeric attributes.
import pandas as pd
x = pd.Series([1, 2, 3, 4, 5])
y = pd.Series([2, 4, 5, 4, 5])
correlation = x.corr(y)
print("Correlation =", correlation)
print("Shomya Sarraf,23053668")