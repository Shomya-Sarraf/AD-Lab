# 4. Rename columns of a DataFrame and drop specified columns.
import pandas as pd
data = pd.DataFrame({
    "oldA": [1,2],
    "oldB": [3,4],
    "remove": ["x","y"]
})
data.rename(columns={"oldA": "A", "oldB": "B"}, inplace=True)
data.drop(columns=["remove"], inplace=True)
print(data)
print("Shomya Sarraf,23053668")