from tkinter import *
frm=Tk()
frm.title("Simple Calculator")
n1=StringVar()
n2=StringVar()
n3=StringVar()

def add():
    ans= str(int(n1.get())+int(n2.get()))
    n3.set(ans)
def sub():
    ans= str(int(n1.get())-int(n2.get()))                   
    n3.set(ans)
def mul():
    ans= str(int(n1.get())*int(n2.get()))
    n3.set(ans)
def div():
    ans= str(int(n1.get())/int(n2.get()))
    n3.set(ans)



l1=Label(frm,text="Enter first number").place(x=20,y=20)
l2=Label(frm,text="Enter second number").place(x=20,y=40)
l3=Label(frm,text="The answer is").place(x=20,y=60)
e1=Entry(frm,textvar=n1).place(x=150,y=20)
e2=Entry(frm,textvar=n2).place(x=150,y=40)
e3=Entry(frm,textvar=n3).place(x=150,y=60)
b1=Button(frm,text="add",command=add).place(x=40,y=100)
b2=Button(frm,text="sub",command=sub).place(x=80,y=100)
b3=Button(frm,text="mul",command=mul).place(x=120,y=100)
b4=Button(frm,text="div",command=div).place(x=160,y=100)
frm.geometry("500x300")
frm.mainloop()