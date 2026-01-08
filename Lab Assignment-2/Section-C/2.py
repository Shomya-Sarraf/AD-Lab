# 2. Count words in a file.
f=open("sample.txt","r")
words=0
for line in f:
    w=line.split()
    words=words+len(w)
print("Total words=",words)
print("Shomya Sarraf, 23053668")