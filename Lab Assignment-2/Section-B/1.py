# 1. Write a function to calculate factorial.
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("Enter number:"))
print("Factorial is : ",fact(n))
print("Shomya Sarraf, 23053668")