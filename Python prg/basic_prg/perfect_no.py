while(True):
    num=int(input("Enter a number or -1 to exit:  "))
    if(num==-1):
        print("Thank you ")
        break
    sum=1
    for i in range(2,num):
        if(num%i==0):
            sum+=i
    if(sum==num):
        print("Number is a perfect number")
    else:
        print("The number is not perfect number")