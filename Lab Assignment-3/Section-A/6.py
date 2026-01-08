# 6. Find unique elements and their counts in a NumPy array.
import numpy as np
arr=np.array([1,2,2,3,3,3,5,4,2])
unique,counts=np.unique(arr,return_counts=True)
print("Unique:",unique)
print("Counts:",counts)
print("Shomya Sarraf, 23053668")