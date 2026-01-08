# 12. Normalize a list of numbers (ML preprocessing concept).
a=[10,20,30,40,50]
mn=min(a)
mx=max(a)
norm=[]
for x in a:
    norm.append((x-mn)/(mx-mn))
print("Normalized=",norm)
print("Shomya Sarraf, 23053668")
