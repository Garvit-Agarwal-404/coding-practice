import csv 
with open("my.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["Name","Age","Sal","City"])
    n=int(input("Enter number of records"))
    for i in range(n):
        Name=input("Enter name")
        Age=int(input("Enter Age"))
        Sal=int(input("Enter Salary"))
        City=input("Enter city name")
        w.writerow([Name,Age,Sal,City])
        