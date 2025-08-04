#this program deals with strings
#multiline string 
a= """
hello what 
is your 
name """
print(a)
#indexing in strings 
b="Hello World"
print(b[6])
print(b[3])
#raw strings 
print(r"Helllo 'what is your /name'?")
#string slicing 
c="Hello,world"
#skipping one letter 
print(c[::2])
#reverse a string
print(c[::-1])

#string methods
d="Hello,world"
#length of string
print(len(d))
#upper case
print(d.upper())
#lower case
print(d.lower())
#split function
print(d.split(","))
#center function 
print(d.center(50))

