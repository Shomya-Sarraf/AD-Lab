# 7. Read a CSV (dataset) and print number of rows (ML useful).
import csv 
f=open("data.csv")
reader=csv.reader(f)
next(reader) 
rows=0
for r in reader:
    rows=rows+1
print("Rows=",rows)
print("Shomya Sarraf, 23053668")
