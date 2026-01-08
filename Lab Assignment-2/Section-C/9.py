# 9. Load a CSV using numpy and print shape.
import numpy as np 
data=np.genfromtxt("data.csv",delimiter=",",skip_header=1)
print("Shape=",data.shape)
print("Shomya Sarraf, 23053668")
