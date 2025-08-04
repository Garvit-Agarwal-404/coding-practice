print("CEASER CIPHER")
def encode():
    in_put=input("Enter your message you want to encode: ")
    shft_no=int(input("Enter the shift number: "))
    encoded_msg=""
    for i in in_put:
        if not i.isalnum():
            encoded_msg+=i
        else:
            hehe=ord(i)+shft_no
            if 122-hehe<0:
                diff=hehe-122
                hehe=96+diff
            encoded_msg+=chr(hehe)
    print(f"Encoded message: {encoded_msg}")    
def decode():
    in_put=input("Enter your message you want to decode: ")
    shft_no=int(input("Enter the shift number: "))
    decoded_msg=""
    for i in in_put:
        if not i.isalnum():
            decoded_msg+=i
        else:
            hehe=ord(i)-shft_no
            if hehe-97<0:
                diff=97-hehe
                hehe=123-diff
            decoded_msg+=chr(hehe)
    print(f"Decoded message: {decoded_msg}")    

restart=True
while(restart):
    choice=input("Type 'encode' to encode and 'decode' to decode: ")
    if(choice=='encode'):
        encode()
    elif(choice=='decode'):
        decode()
    restart_choice=input("Do you want to continue 'Y' or 'N': ").lower()
    if(restart_choice=='n'):
        restart=False

