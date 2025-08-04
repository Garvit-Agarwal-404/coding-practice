
try:
    c=0
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    
    c=a/b
except ZeroDivisionError as msg:
    print(msg)
except ValueError as msg:
    print(msg)

finally:
    print("Mai to execute hounga")
