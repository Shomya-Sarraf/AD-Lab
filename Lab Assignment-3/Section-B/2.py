# 2. Read a CSV and check for missing values column-wise.
import numpy as np 
import pandas as pd
data=pd.DataFrame({
    "A":[1,2,np.nan],
    "B":["x",None,"z"]
})
print(data.isnull().sum())
print("Shomya Sarraf,23053668")