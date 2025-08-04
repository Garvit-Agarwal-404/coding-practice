def fact(a):
    prod=1
    for i in range(1,a+1):
        prod*=i
    return prod
n=int(input("Enter the number you want to check for armstrong: "))
t=n
sum=0
while (n!=0):
    last=n%10
    pp=fact(last)
    sum+=pp
    n=n//10
if(sum==t):
    print("the number is armstrong")
else:
    print("the number is not armstrong")