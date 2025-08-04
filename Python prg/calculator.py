#this is a basic calculator 
def calc():
    a=int(input("Enter first number: "))
    sign=input("Enter the operator: ")
    b=int(input("Enter second number: "))
    if (sign=='+'):
        ans=a+b
        return print(ans)
    elif (sign=='-'):
        ans=a-b
        return print(ans)
    elif (sign=='*'):
        ans=a*b
        return print(ans)
    elif (sign=='/'):
        ans=a/b
        return print(ans)
    elif (sign=='//'):
        ans=a//b
        return print(ans)
    elif (sign=='**'):
        ans=a**b
        return print(ans)
    else:
        return print("Invalid Command")
calc()   
