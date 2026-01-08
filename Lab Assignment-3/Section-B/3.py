# 3. Replace missing values using mean for numeric columns and mode for categorical ones.
import pandas as pd
import numpy as np 

data = pd.DataFrame({
    "age": [25, np.nan, 30],
    "gender": ["M", None, "F"]
})

data["age"] = data["age"].fillna(data["age"].mean())
data["gender"] = data["gender"].fillna(data["gender"].mode()[0])

print(data)
print("Shomya Sarraf,23053668")
