def prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if (count==0):
        print("The number is a prime number")
    else:
        print("The number is not a prime number")
prime(12)