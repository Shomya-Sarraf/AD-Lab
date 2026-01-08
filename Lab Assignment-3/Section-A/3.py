# 3. Generate a 3×3 identity matrix and multiply it with a 3×3 matrix of your choice.
import numpy as np 
I=np.eye(3)
A=np.array([[2,3,1],
            [4,5,6],
            [7,8,9]])
print("Identity:\n",I)
print("Matrix A:\n",A)
result=I.dot(A)
print("Result:\n",result)
print("Shomya Sarraf, 23053668")