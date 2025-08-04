#Normal Function
def my_fun():
    print("This is my function")
my_fun()
'''Postional Arguments: The arguments are to be declared in the 
   same order as in parameters. '''
def Posi_fun(name,age):
    print(f"My name is {name}.")
    print(f"My age is {age}.")
Posi_fun("Garvit",19)
''' Keyword Arguments: The order of arguments can be changed as they as
    assigned a keyword in accordance with the paramter name.'''
def Keyword_fun(gender,name,age):
    print(f"I am a {gender}")
    print(f"My name is {name}.")
    print(f"My age is {age}.")
Keyword_fun("Male",age=20,name="Bisi")
'''Default Arguments: A default value is assigned.'''
def default_fun(gender,name,age=18):
    print(f"I am a {gender}")
    print(f"My name is {name}.")
    print(f"My age is {age}.")
default_fun("Male","Hehe")
'''Arbitary-Keywords Arguements: Arbitary(variable)
    number of arguments can be passed'''
"""(1)using *args: non-keyword arguments"""
def arb_kw1(*args):
    for arg in args:
        print(arg)
arb_kw1("Hello","Garvit","Bull")
"""(2)using **kwargs:using keyword arguements"""
def arb_kw2(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
arb_kw2(name="Garvit",Class=7,age=7)