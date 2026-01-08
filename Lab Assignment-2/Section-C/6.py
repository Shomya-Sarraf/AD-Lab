# 6. Write a program to find average of numbers stored in a file.
f=open("numbers.txt","r")
total=0
count=0
for line in f:
    total=total+float(line)
    count=count+1
avg=total/count
print("Average=",avg)
print("Shomya Sarraf, 23053668")
