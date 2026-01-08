# 10. Replace missing values in a file with the mean value.
f=open("nums.txt","r")
vals=[]
for line in f:
    line=line.strip()
   
    if line =="":
        vals.append(None)    
    else:
        vals.append(float(line))
    

total=0
count=0
for x in vals:
    if x is not None:
        total=total+x
    count=count+1
mean=total/count
new=[]
for x in vals:
    if x is None:
        new.append(mean)
    else:
        new.append(x)
print("After filling missing:",new)
print("Shomya Sarraf, 23053668")

    
