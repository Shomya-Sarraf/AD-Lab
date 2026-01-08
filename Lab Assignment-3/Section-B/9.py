# 9. Sort a DataFrame on two different columns (one asc, one desc).
import pandas as pd 
data=pd.DataFrame({
    "age":[30,45,50],
    "score":[80,98,97]
})
print(data.sort_values(by=["age","score"],ascending=[True,False]))
print("Shomya Sarraf,23053668")