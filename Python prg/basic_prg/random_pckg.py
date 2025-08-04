import random 
lst=[1,2,3,4]
print(random.randint(10,20))          # random integer between and inclduing the param
print(random.randrange(30,40,2))      # (start,stop,step) random integer between the given range
print(random.random())                # a random float number 
print(random.choice(lst))             # choose random element from th sequence    
random.shuffle(lst)                   # shuffles the *MUTABLE SEQUENCE* inplace     
print(lst)                                