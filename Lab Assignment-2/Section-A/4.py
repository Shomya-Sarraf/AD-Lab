# 4. Find the second largest element in a list.
a=[1,5,4,7]
mx=max(a)
second=-9999
for x in a:
    if x!=mx and x>second:
        second=x
    
print(second)
print("Shomya Sarraf, 23053668")