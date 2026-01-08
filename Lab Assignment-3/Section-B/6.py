# 6. Add a new column “BMI” using height & weight data (BMI = weight / height²).
import pandas as pd
data = pd.DataFrame({
    "height": [1.7, 1.6],
    "weight": [70, 60]
})
data["BMI"] = data["weight"] / (data["height"] ** 2)
print(data)
print("Shomya Sarraf,23053668")
