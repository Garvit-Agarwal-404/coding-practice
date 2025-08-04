import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
no_of_letters=int(input("How many letters will you like in your password?"))
no_of_symbols=int(input("How many symbols will you like?"))
no_of_no=int(input("How many numbers will you like?"))
password=[]
for i in range(0,no_of_letters):
    password.append(random.choice(letters))
for i in range(0,no_of_symbols):
    password.append(random.choice(symbols))
for i in range(0,no_of_no):
    password.append(random.choice(numbers))
random.shuffle(password)
final_pass=''
for i in password:
    final_pass+=''.join(i)
print(final_pass)

