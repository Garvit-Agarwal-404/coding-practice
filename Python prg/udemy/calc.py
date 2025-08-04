def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculator():
    valid=True
    num1=float(input("Enter the first number: "))
    while(valid):
        
        for i in operations:
            print(i)
        sign=input("Enter a operator from the above: " )
        num2=float(input("Enter the next number: "))
        result=operations[sign](num1,num2)
        print(f"{num1} {sign} {num2} = {result}")
        choice=input("Do you want to continue using the same result (y) or want to start a new calculation(n)?").lower()
        if choice=='y':
            num1=result
        elif choice=='n':
            valid=False
            print("\n"*20)
            calculator()

calculator()
