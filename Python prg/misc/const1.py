class abc:
    n=20
    
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def set(self):
        self.name=input("Enter your name ")
        self.age=int(input("Enter your age "))
        self.sal=int(input("Enter your sal")) 
    def show(self):
        print(self.name,self.age,self.sal,self.n)
    def del_1(self):
        del self.name

a1=abc("garvit",12,345)
a1.set()
a1.show()

a2=abc("sksk ",2,12)
a2.city="Alwar"
a2.show()
a2.del_1()
print(a2.__dict__)

