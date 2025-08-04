s=str(input("Enter a string"))
palindrome=False
str_to_lower=s.lower()
str_rer=str_to_lower[::-1]
if str_to_lower==str_rer:
    palindrome=True
    print("It is a PAlindorme")
else:
    print("Not a palindorme")