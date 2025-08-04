# with open("aa","r") as f:
#     data=f.read()
#     for char in data:
#         if(char.isdigit()):
#             print(char)

with open("aa","r") as f:
    data=f.read()
    count=0
    for char in data:
        if(char.isdigit()):
            count=count+1
print(count)