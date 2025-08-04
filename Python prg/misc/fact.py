def fact(n):
    # if n<0
    if n<0:
        print("Invalid")
    elif n==0:
        return 1
    else:
        return(n*fact(n-1))
x=int(input("Enter the factorial you want to calcluate"))
print("The answer is ",fact(x))