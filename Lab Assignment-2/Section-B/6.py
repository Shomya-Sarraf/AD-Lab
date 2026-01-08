# 6. Write a function to compute nCr (Combination).
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def nCr(n,r):
    return fact(n) // (fact(r)*fact(n-r))
n=int(input("Enter n:"))
r=int(input("Enter r:"))
print(nCr(n,r))
print("Shomya Sarraf, 23053668")