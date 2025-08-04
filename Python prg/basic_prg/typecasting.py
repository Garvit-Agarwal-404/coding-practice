#implicit typecasting
a,b=1,2.5
print(a+b)

#explicit typecasting
a=1
b='2'
print(a+int(b))

c=5
print(float(c))
c='a'
print(ord(c))
z=("","")
print(type(z))