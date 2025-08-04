#is an unorganised collection of data in which data is stored in a key-value pair 
#it is in the format {"Key":"Value"}
my_dict={1:"Garvit",2:"Ravi",3:"Hari",}

for i in my_dict:
    print(i,":",my_dict[i])
#if you want to reinntialize  a dictionary thne you should do like this 
# my_dict={}
# print(my_dict)

#if we want to chnage a element in the dictionary
my_dict[2]="Vishnu"
print(my_dict)
#nested dictionary
#(1)list in dictionary
cities_visited={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Munich","Frankfurt"],
    "India":["Delhi","Mumbai","Jaipur"],

} 
print(cities_visited["France"][0])

nested_list=[1,2,[3,4]]
#to print 4
print(nested_list[2][1])
