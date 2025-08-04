#functions with outputs
def name(f_name,l_name):
    full_name=(f_name+" "+ l_name).title()
    return full_name
f_name=input("Enter your first name: ")
l_name=input("Enter your last name: ")
naam=name(f_name,l_name)
print(naam)

# *args example
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum 
print(sum(1,2,3,4,5))