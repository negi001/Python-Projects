########################################## __author__ == "AYUSH NEGI"#################################################

import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror

win = Tk()
win.title("Calculator")
win.geometry('430x445+0+0')
win.resizable(0, 0)

pos = 0

def clear_all():
    ent.delete(0, "end")


def seven():
    global pos
    pos += 1
    ent.insert(pos, '7')


def eight():
    global pos
    pos += 1
    ent.insert(pos, '8')


def nine():
    global pos
    pos += 1
    ent.insert(pos, '9')


def four():
    global pos
    pos += 1
    ent.insert(pos, '4')


def five():
    global pos
    pos += 1
    ent.insert(pos, '5')


def six():
    global pos
    pos += 1
    ent.insert(pos, '6')


def one():
    global pos
    pos += 1
    ent.insert(pos, '1')


def two():
    global pos
    pos += 1
    ent.insert(pos, '2')


def three():
    global pos
    pos += 1
    ent.insert(pos, '3')


def zero():
    global pos
    pos += 1
    ent.insert(pos, '0')


def div():
    global pos
    ent.insert(pos, '/')


def res():
    global a
    try:
        a = eval(str(ent.get()))
        ent.delete(0, 'end')
        ent.insert(0, a)
    except Exception as e:
        ent.delete(0, 'end')
        ent.insert(0, e)


def add():
    global pos
    pos += 1
    ent.insert(pos, "+")


def sub():
    global pos
    pos += 1
    ent.insert(pos, '-')


def mul():
    global pos
    pos += 1
    ent.insert(pos, '*')


def clrs():
    global pos
    global a
    ent.delete(pos-1, 'end')
    pos -= 1


f = Frame(win, relief='groove')
f.pack(side=TOP)
ent = Entry(f, width=70, relief='groove', font=("Roboto 14 bold"),
            bd=2, justify="right", fg="green", bg='black')
ent.pack(side=TOP, ipady=15)

z = Frame(win)
z.pack(side=TOP)
aclr = Button(z, text="AC", font=('Roboto 10 bold'),
              relief='groove', command=clear_all, bg='orange', fg='white')
aclr.pack(side=LEFT, ipady=15, fill=X, ipadx=95)
back = Button(z, text="C", relief='groove', fg='white',
              bg='orange', font=('Roboto 10 bold'), command=clrs)
back.pack(side=LEFT, ipady=15, ipadx=120)

f1 = Frame(win)
f1.pack(fill=X)
btn1 = Button(f1, text="7", font=('Roboto 10 bold'),
              relief='groove', command=seven, bg='blue', fg='white')
btn1.pack(side=LEFT, ipadx=45, ipady=20)
btn2 = Button(f1, text="8", font=('Roboto 10 bold'),
              relief='groove', command=eight, bg='blue', fg='white')
btn2.pack(side=LEFT, ipadx=45, ipady=20)
btn3 = Button(f1, text="9", font=('Roboto 10 bold'),
              relief='groove', command=nine, bg='blue', fg='white')
btn3.pack(side=LEFT, ipadx=45, ipady=20)
btn4 = Button(f1, text="/", font=('Roboto 10 bold'),
              relief='groove', command=div, bg='blue', fg='white')
btn4.pack(side=LEFT, ipadx=45, ipady=20)

f2 = Frame(win)
f2.pack(fill=X)
btn5 = Button(f2, text="4", font=('Roboto 10 bold'),
              relief='groove', command=four, bg='blue', fg='white')
btn5.pack(side=LEFT, ipadx=45, ipady=20)
btn6 = Button(f2, text="5", font=('Roboto 10 bold'),
              relief='groove', command=five, bg='blue', fg='white')
btn6.pack(side=LEFT, ipadx=45, ipady=20)
btn7 = Button(f2, text="6", font=('Roboto 10 bold'),
              relief='groove', command=six, bg='blue', fg='white')
btn7.pack(side=LEFT, ipadx=45, ipady=20)
btn8 = Button(f2, text="*", font=('Roboto 10 bold'),
              relief='groove', command=mul, bg='blue', fg='white')
btn8.pack(side=LEFT, ipadx=45, ipady=20)

f3 = Frame(win)
f3.pack(fill=X)
btn9 = Button(f3, text="1", font=('Roboto 10 bold'),
              relief='groove', command=one, bg='blue', fg='white')
btn9.pack(side=LEFT, ipadx=45, ipady=20)
btn10 = Button(f3, text="2", font=('Roboto 10 bold'),
               relief='groove', command=two, bg='blue', fg='white')
btn10.pack(side=LEFT, ipadx=45, ipady=20)
btn11 = Button(f3, text="3", font=('Roboto 10 bold'),
               relief='groove', command=three, bg='blue', fg='white')
btn11.pack(side=LEFT, ipadx=45, ipady=20)
btn12 = Button(f3, text="-", font=('Roboto 10 bold'),
               relief='groove', command=sub, bg='blue', fg='white')
btn12.pack(side=LEFT, ipadx=45, ipady=20)


def dot():
    global pos
    pos += 1
    ent.insert(pos, '.')


f3 = Frame(win)
f3.pack()
btn10 = Button(f3, text=".", font=('Roboto 10 bold'),
               relief='groove', command=dot, bg='blue', fg='white')
btn10.pack(side=LEFT, ipadx=63, ipady=20)
btn9 = Button(f3, text="0", font=('Roboto 10 bold'),
              relief='groove', command=zero, bg='blue', fg='white')
btn9.pack(side=LEFT, ipadx=63, ipady=20)
btn11 = Button(f3, text="+", font=('Roboto 10 bold'),
               relief='groove', command=add, bg='blue', fg='white')
btn11.pack(side=LEFT, ipadx=63, ipady=20)

eql = Button(win, text="=", font=('Roboto 12 bold'),
             relief='groove', command=res, bg='orange', fg='white')
eql.pack(side=TOP, fill=X, ipady=15)

win.mainloop()
########################################################################################################################