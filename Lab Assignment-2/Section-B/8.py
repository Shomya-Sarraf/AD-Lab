# 8. Write a function to compute square root without using math library.
def squareRoot(n):
    x=0
    while x*x<=n:
        x+=1
    return x-1
n=int(input("Enter number:"))
print(squareRoot(n))
print("Shomya Sarraf, 23053668")
