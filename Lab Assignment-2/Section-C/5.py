# 5. Read a CSV file and print column names.
import csv 
f=open("data.csv")
reader=csv.reader(f)
header=next(reader)
print("Columns:",header)
print("Shomya Sarraf, 23053668")