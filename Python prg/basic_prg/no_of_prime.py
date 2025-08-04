def is_prime(n3):
    if n3<=1:
        return False
    for i in range(2,n3):
        if(n3%i==0):
            return False
    else:
        return True
def no_of_prime(n1,n2):
    count=0
    for i in range(n1,n2+1):
        if(is_prime(i)==True):
            count+=1
    return print(f"There are {count} prime numbers between {n1} and {n2}")


n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
no_of_prime(n1,n2)