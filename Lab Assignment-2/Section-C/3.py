# 3. Count characters in a file.
f=open("sample.txt","r")
chars=0
for line in f:
    chars=chars+len(line)
print("Characters=",chars)
print("Shomya Sarraf, 23053668")