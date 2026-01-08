# 10.Create a 5×5 matrix and calculate row-wise and column-wise sums.
import numpy as np
mat=np.arange(1,26).reshape(5,5)
print("Matrix:\n",mat)
print("Row sums:",mat.sum(axis=1))
print("Column sums:",mat.sum(axis=0))
print("Shomya Sarraf, 23053668")