a=list(map(lambda x:x*x*x,[x for x in range(1,10)]))
print(a)


# adding elements for two lists
l1=[1,2,3,4,5]
l2=[10,9,8,7,6]
b=list(map(lambda x,y:x+y,l1,l2))
print(b)