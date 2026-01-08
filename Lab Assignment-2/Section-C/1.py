# 1. Write a program to count number of lines in a text file.
f=open("sample.txt","r")
count=0
for line in f:
    count=count+1
print("Total lines: ",count)
print("Shomya Sarraf, 23053668")