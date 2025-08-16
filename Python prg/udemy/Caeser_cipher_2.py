alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_or_decode(choice,message,shft_no):
    out=""
    if(choice=="decode"):
        shft_no*=-1
    for i in message:
        if i not in alphabet:
            out+=i
        else:
            shft_pstn=(alphabet.index(i)+shft_no)%len(alphabet)
            out+=alphabet[shft_pstn]
    return out

valid=True
while(valid):
    choice=input("Do you want to encode or decode? ").lower()
    message=input("Enter the message: ").lower()
    shft_no=int(input("Enter the shift number: "))
    result=encode_or_decode(choice,message,shft_no)
    print(f"{choice} Message: {result}")
    cnt_choice=input("Do you want to continue(YES) or no(NO)? ").lower()
    if(cnt_choice!="yes"):
        break