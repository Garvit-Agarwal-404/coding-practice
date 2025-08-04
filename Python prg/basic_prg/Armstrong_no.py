def no_of_digits(a):
    count=0 
    if(a==0):
        count=1
    while(a!=0):
        a=a//10
        count+=1
    return count
while(True):
    # n=int(input("Enter a number you want to check for Armstrong: "))
    # if(n==0):
    #     print("Number is not Armstrong")
    #     break
    sum=0
    t=n
    for t in range(0,1001):
        while(n!=0):

            last=n%10
            power=last**no_of_digits(t)
            sum+=power
            n=n//10
        if(sum==t):
            print(t)
        else:
            pass



