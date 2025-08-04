from tkinter import *
import math

frm = Tk()
frm.title("Scientific Calculator")
v = StringVar()

a = 0
b = 0
opt = ""

def fun(s):
    global a
    global b
    global opt
    if s in ('+', '-', '*', '/'):
        a = float(v.get())
        v.set("")
        opt = s
    elif s == '=':
        b = float(v.get())
        if opt == '+':
            v.set(a + b)
        elif opt == '-':
            v.set(a - b)
        elif opt == '*':
            v.set(a * b)
        elif opt == '/':
            if b != 0:
                v.set(a / b)
            else:
                v.set("Error")
    elif s == 'sin':
        a = float(v.get())
        v.set(math.sin(math.radians(a)))
    elif s == 'cos':
        a = float(v.get())
        v.set(math.cos(math.radians(a)))
    elif s == 'tan':
        a = float(v.get())
        v.set(math.tan(math.radians(a)))
    elif s == 'sq':
        a = float(v.get())
        v.set(a * a)
    elif s == 'sqr':
        a = float(v.get())
        if a >= 0:
            v.set(math.sqrt(a))
        else:
            v.set("Error")
    elif s == 'log':
        a = float(v.get())
        if a > 0:
            v.set(math.log10(a))
        else:
            v.set("Error")
    else:
        current = v.get()
        v.set(current + str(s))

e1 = Entry(frm, textvar=v)
e1.place(x=20, y=20, height=30, width=230)

b0 = Button(frm, text=0, command=lambda: fun(0))
b0.place(x=20, y=60, height=20, width=20)

b1 = Button(frm, text=1, command=lambda: fun(1))
b1.place(x=50, y=60, height=20, width=20)

b2 = Button(frm, text=2, command=lambda: fun(2))
b2.place(x=80, y=60, height=20, width=20)

b3 = Button(frm, text=3, command=lambda: fun(3))
b3.place(x=110, y=60, height=20, width=20)

b4 = Button(frm, text=4, command=lambda: fun(4))
b4.place(x=140, y=60, height=20, width=20)

b5 = Button(frm, text=5, command=lambda: fun(5))
b5.place(x=20, y=90, height=20, width=20)

b6 = Button(frm, text=6, command=lambda: fun(6))
b6.place(x=50, y=90, height=20, width=20)

b7 = Button(frm, text=7, command=lambda: fun(7))
b7.place(x=80, y=90, height=20, width=20)

b8 = Button(frm, text=8, command=lambda: fun(8))
b8.place(x=110, y=90, height=20, width=20)

b9 = Button(frm, text=9, command=lambda: fun(9))
b9.place(x=140, y=90, height=20, width=20)

ba = Button(frm, text='+', command=lambda: fun('+'))
ba.place(x=20, y=120, height=20, width=20)

bs = Button(frm, text='-', command=lambda: fun('-'))
bs.place(x=50, y=120, height=20, width=20)

bm = Button(frm, text='*', command=lambda: fun('*'))
bm.place(x=80, y=120, height=20, width=20)

bd = Button(frm, text='/', command=lambda: fun('/'))
bd.place(x=110, y=120, height=20, width=20)

be = Button(frm, text='=', command=lambda: fun('='))
be.place(x=140, y=120, height=20, width=80)

bsin = Button(frm, text='sin', command=lambda: fun("sin"))
bsin.place(x=170, y=60, height=20, width=40)

bcos = Button(frm, text='cos', command=lambda: fun("cos"))
bcos.place(x=210, y=60, height=20, width=40)

btan = Button(frm, text='tan', command=lambda: fun("tan"))
btan.place(x=250, y=60, height=20, width=40)

bsq = Button(frm, text='sq', command=lambda: fun("sq"))
bsq.place(x=170, y=90, height=20, width=40)

bsqr = Button(frm, text='sqr', command=lambda: fun("sqr"))
bsqr.place(x=210, y=90, height=20, width=40)

blog = Button(frm, text='log', command=lambda: fun("log"))
blog.place(x=250, y=90, height=20, width=40)

bde = Button(frm, text='.', command=lambda: fun('.'))
bde.place(x=250, y=120, height=20, width=40)

frm.geometry("300x170")
frm.mainloop()
