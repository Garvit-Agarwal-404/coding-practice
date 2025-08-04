def fibo(n):
    #if n<=0
    if n<=0:
         print("Invalid input")
    #if n=1    
    elif n==1:
         return 0
    #if n=2
    elif n==2:
         return 1
    #if n>2
    else:
         return fibo(n-1)+fibo(n-2)
         
n=int(input("Enter the nth fibo number you want"))
print("The", n,"th fibo number is", fibo(n))