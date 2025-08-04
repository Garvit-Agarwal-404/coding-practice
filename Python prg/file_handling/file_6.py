import csv
with open("my.csv","r") as f:
    r=csv.reader(f)
    data=list(r)
    for line in data:
        for val in line:
            print(val,end=" ")
        print()    
        