# 12. Create a matrix and remove duplicate rows using NumPy.
import numpy as np
mat=np.array([[1,2,3],
             [4,5,6],
             [1,2,3],
             [7,8,9],
             [4,5,6]])
unique_rows=np.unique(mat,axis=0)
print("Unique rows:\n",unique_rows)
print("Shomya Sarraf, 23053668")