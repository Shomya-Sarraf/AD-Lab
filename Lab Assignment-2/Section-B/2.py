# 2. Write a function to check prime number.
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
n=int(input("Enter number:"))
print(is_prime(n))
print("Shomya Sarraf, 23053668")