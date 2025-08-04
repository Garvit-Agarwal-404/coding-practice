
l=[]
type(l)
<class 'list'>
l=[1,2,3,4,"nitin","ajay",1,"alwar"]
print(l)
[1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar']
type(l)
<class 'list'>
t=(1,2,3,4,"nitin","ajay",1,"alwar")
print(t)
(1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar')
type(t)
<class 'tuple'>
l[2]
3
t[2]
3
l[3]="sonu"
l
[1, 2, 3, 'sonu', 'nitin', 'ajay', 1, 'alwar']
t[3]="sonu"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t[3]="sonu"
TypeError: 'tuple' object does not support item assignment
i=0
while(i<len(t)):
    print(t[i])
    i=i+1

    
1
2
3
4
nitin
ajay
1
alwar

>>> 
>>> for i in l:
...     print(i)
... 
...     
1
2
3
sonu
nitin
ajay
1
alwar
>>> 
>>> l=[1,2,3,4,5,6,7,8,9]
>>> print(l[0:5])
[1, 2, 3, 4, 5]
>>> print(l[0:8:2])
[1, 3, 5, 7]
>>> print(l[0:8:])
[1, 2, 3, 4, 5, 6, 7, 8]
>>> print(l[:8:])
[1, 2, 3, 4, 5, 6, 7, 8]
>>> print(l[::])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(l[3::])
[4, 5, 6, 7, 8, 9]
>>> print(l[3::2])
[4, 6, 8]
>>> print(l[:7:2])
[1, 3, 5, 7]
>>> l+l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> t+t
(1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar', 1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar')
>>> l*4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> t*4
(1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar', 1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar', 1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar', 1, 2, 3, 4, 'nitin', 'ajay', 1, 'alwar')
