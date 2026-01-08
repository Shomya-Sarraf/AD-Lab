# 10. Merge two DataFrames using inner join, outer join, left join, right join.10. Merge two DataFrames using inner join, outer join, left join, right join.
import pandas as pd
a = pd.DataFrame({"id": [1,2], "A": ["x","y"]})
b = pd.DataFrame({"id": [2,3], "B": ["p","q"]})
print("Inner:\n", pd.merge(a, b, on="id", how="inner"))
print("Left:\n", pd.merge(a, b, on="id", how="left"))
print("Right:\n", pd.merge(a, b, on="id", how="right"))
print("Outer:\n", pd.merge(a, b, on="id", how="outer"))
print("Shomya Sarraf,23053668")