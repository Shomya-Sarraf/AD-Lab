 
# 1. Find max and min from a list without using built-ins.
a=[5,2,9,1,7]
max=a[0]
min=a[0]
for x in a:
    if x>max:
        max=x
    if x<min:
        min=x
print(max)
print(min)
print("Shomya Sarraf, 23053668")