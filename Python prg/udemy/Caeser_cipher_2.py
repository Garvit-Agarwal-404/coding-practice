alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(original_msg,shift_num,encode_or_decode):
    cipher_text=""
    if(encode_or_decode=='decode'):
                shift_num*=-1
    
    for i in original_msg:
        if i not in alphabet:
            cipher_text+=i
        else:
            shifted_position=alphabet.index(i)+shift_num
            shifted_position%=len(alphabet)
            cipher_text+=alphabet[shifted_position]
    print(f"The {encode_or_decode} message is {cipher_text}")

valid=True
while(valid):
    choice=input("Do you want to encode or decode? ").lower()
    message=input("Enter the message: ").lower()
    shft_no=int(input("Enter the shift number: "))
    caeser(message,shft_no,choice)
    cont_choice=input("Do you want to continue (Y or N) ?").lower()
    if(cont_choice=='y'):
        continue
    elif(cont_choice=='n'):
        valid=False