# 11. Compute correlation between two lists.
x=[1,2,3,4,5]
y=[2,3,5,7,8]
#calculate mean
mx=sum(x)/len(x)
my=sum(y)/len(y)
num=0
dx2=0
dy2=0
for i in range(len(x)):
    dx=x[i]-mx
    dy=y[i]-my
    num=num+dx*dx
    dx2=dx2+dx*dx
    dy2=dy2+dy*dy
corr=num/((dx2**0.5)*(dy2**0.5))
print("Correlation is : ",corr)
print("Shomya Sarraf, 23053668")
