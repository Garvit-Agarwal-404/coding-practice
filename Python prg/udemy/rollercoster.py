print("WELCOME TO THE ROLERCOSTER!!")
height=int(input("Enter your height in cm: "))
if(height>=120):
    print("You are allowed to sit on the roller coster !!")
    age=int(input("Enter your age: "))
    if(age>=18):
        print("You have to pay $10.")
    else:
        print("You ahve to pay $7.")
else:
    print("Sorry, you cant sit on the roller coster !!")