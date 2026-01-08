# 4. Write a function to return unique elements from a list.
def unique(a):
    new=[]
    for x in a:
        if x not in new:
            new.append(x)
    return new
a=[1,2,3,4,4,2,3]
print(unique(a))
print("Shomya Sarraf, 23053668")