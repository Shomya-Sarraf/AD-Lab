# 5. Sort a list manually (bubble sort logic)
a=[5,3,2,7]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]       
print(a)
print("Shomya Sarraf, 23053668")