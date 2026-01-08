# 1. Load a CSV file and display only the rows where a given column has values above its column mean.
import pandas as pd 
data=pd.DataFrame({
    "score":[50,80,60,90]
})
mean_values=data["score"].mean()
result=data[data["score"]>mean_values]
print("Mean:",mean_values)
print(result)
print("Shomya Sarraf,23053668")
