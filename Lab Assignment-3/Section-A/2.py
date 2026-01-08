# 2. Write a program to create a 1D NumPy array and normalize it (scale between 0 and 1).
import numpy as np
arr=np.array([5,10,15,20,25],dtype=float)
print("Original:",arr)
arr_min=arr.min()
arr_max=arr.max()
normalized=(arr-arr_min)/(arr_max-arr_min)
print("Normalized:",normalized)
print("Shomya Sarraf, 23053668")