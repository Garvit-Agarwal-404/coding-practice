from tkinter import *
frm=Tk()

s1=StringVar()
s2=StringVar()
s3=StringVar()
def fun1():
	print("Click me press",s1.get(),s2.get(),s3.get())
	
	

def fun2():
	s1.set("Garvit")
	s2.set("19")
	s3.set("56789")




l1=Label(frm,text="Enter name").place(x=20,y=40)
l2=Label(frm,text="Enter age").place(x=20,y=60)
l3=Label(frm,text="Enter sal").place(x=20,y=80)
e1=Entry(frm,textvar=s1).place(x=80,y=40)
e2=Entry(frm,textvar=s2).place(x=80,y=60)
e3=Entry(frm,textvar=s3).place(x=80,y=80)
b1=Button(frm,text="Click ME",command=fun1).place(x=80,y=100)
b2=Button(frm,text="Hit ME",command=fun2).place(x=120,y=100)
frm.geometry("500x300")
frm.mainloop()
