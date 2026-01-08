# 8. Group rows by a categorical variable and compute aggregate statistics.
import pandas as pd 
data=pd.DataFrame({
    "city":["A","A","B"],
    "sales":[100,150,200]
})
print(data.groupby("city")["sales"].sum())
print("Shomya Sarraf,23053668")