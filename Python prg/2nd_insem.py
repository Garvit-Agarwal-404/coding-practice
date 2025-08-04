# class demo:
#     def __init__(self):
#         self.user_string=" "
#     def get_string(self):
#         self.user_string=input("Enter a string:")
#     def print_string(self):
#         print("String in upper case", self.user_string.upper())
# demo_object=demo()
# demo_object.get_string()
# demo_object.print_string()


# def hello(input_string):
#     words=input_string.split()
#     result=[]
#     for word in words:
#         if word.lower().startswith('a') or word.lower().startswith('e'):
#             result.append(word)
#     return result
# input_string="Hii my ear is able to hear a noise."
# final_result=hello(input_string)    
# print(final_result)

def hello(words,text):
    found_words=[]
    for word in words:
        if word in text:
            found_words.append(word)
    return found_words
text="Hello my name is garvit."
words=['my','garvit']
result=hello(words,text)
print(result)