# #empty list
a=[]

# creating a list
"""Method-1"""
lst=[1,2,3,4,5]
print(lst)
"""(2) method 2"""
b=[]
for i in range(6):
    b.append(i)
print(b)
"""(3) method 3"""
c=list(range(6))
print(c)
"""method-4"""
lst_1=[0 for i in range(5)] 
print(lst_1)
lst_2=[i for i in range(5)]
print(lst_2)
"""using eval() method"""
d=eval(input("Enter a string for eval function"))
print(d)
print(type(d))

""" handling single line string input as int input"""
l=input().split()
u=[]
for i in l:
  u.append(int(i))
print(u)

inp1=int(input())
l=[]
for i in range(inp1):
    inp2=int(input())
    l.append(inp2)
print(l)
#adding element to list:
"""using append(): appends a value to the last of the list """
lst_3=[1,2]
lst_3.append(3)
print(lst_3)

"""using insert(index,value): inserts a value to a particular index"""
lst_4=[1,2,3,4,5,6]
lst_4.insert(2,[10,20])
print(lst_4)
"""using extend(): adds multiple items to the end of the list"""
lst_5=[1,5,6,8,9]
lst_5.extend([4,7,67,89])
print(lst_5)
"""enumerate function"""
print(lst_5.count(4))
for index,value in enumerate(lst_5):
    print(f"Index: {index},Value: {value}")


#removing elements:
"""clear():removes all the elements from the list"""
lst_10=[1,2,3,4,5]
lst_10.clear()
print(lst_10)
"""remove(value): removes the first occurance of a specifies value"""
lst_11=[11,12,13,14,12,15]
lst_11.remove(12)
print(lst_11)
"""pop(index): removes and returns the elememt at the given index or if no index is given 
then it removes and returns the last element in the list """
lst_16=[16,17,18,19,20]
lall=lst_16.pop(3)
print(lall)

# list aliasing and copying:
