# 8. Generate two random arrays and compute cosine similarity.
import numpy as np
a=np.random.rand(5)
b=np.random.rand(5)
dot=np.dot(a,b)
cosine_sim=dot/(np.linalg.norm(a)*np.linalg.norm(b))
print("a:",a)
print("b:",b)
print("Cosine Similarity:",cosine_sim)
print("Shomya Sarraf, 23053668")