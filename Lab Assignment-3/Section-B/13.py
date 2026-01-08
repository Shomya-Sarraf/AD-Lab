# 13. Drop duplicate rows and print how many rows were removed.
import pandas as pd
data = pd.DataFrame({
    "A": [1,2,1,3]
})
print("Before:\n", data)
print("After:\n", data.drop_duplicates())
print("Shomya Sarraf,23053668")