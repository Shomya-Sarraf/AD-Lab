# 5. Write a function to count uppercase and lowercase letters in a string.
def count(s):
    up=0
    low=0
    for ch in s:
        if 'A'<=ch<='Z':
            up+=1
        elif 'a'<=ch<='z':
            low+=1
    return up,low
s=input("Enter string:")
u,l=count(s)
print("Uppercase=",u)
print("Lowercase=",l)
print("Shomya Sarraf, 23053668")