# 7. Write a function to check if a number is perfect.
def isPerfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s==n
n=int(input("Enter number:"))
print(isPerfect(n))
print("Shomya Sarraf, 23053668")