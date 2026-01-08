# 15. Implement a simple kNN step: find nearest value from a list.
numbers=[2.0,4.8,5.7,6.1]
test=3.7
nearest=None
smallest=None
for n in numbers:
    d=abs(n-test)
    if smallest==None or d<smallest:
        smallest=d
        nearest=n
print("Nearest=",nearest)
print("Shomya Sarraf, 23053668")