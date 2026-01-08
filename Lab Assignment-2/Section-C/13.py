# 13. Standardize a list of numbers manually.
a=[10,20,30,40]
mean=sum(a)/len(a)
sd=(sum((x-mean)**2 for x in a)/len(a))**0.5
std=[]
for x in a:
    std.append((x-mean)/sd)
print("Standardized:",std)
print("Shomya Sarraf, 23053668")