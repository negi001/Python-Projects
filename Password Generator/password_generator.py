'''Random Password Generator in Python'''
'''CREATED BY AYUSH NEGI'''
'''DATE: 29/09/2020'''

'''Importing necessary modules for project'''
import os
import random
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
# import pymysql as MySQLdb

'''Main window'''
win = Tk()
win.title('Password Generator')
win.geometry('550x350')
win.configure(bg='black')
win.resizable(0,0)

''' global boolean '''
firstclick = True

'''
Name : on_first_click
purpose : to remove the placeholder text on click
'''
def on_first_click(event):
    global firstclick
    if firstclick:
        firstclick = False
        ent.delete(0,'end')

'''
Name : addToClipboard
purpose : to copy text to clipboard
'''
def addToClipboard():
    global f
    command = 'echo | set /p nul=' + f.strip() + '| clip'
    os.system(command) 
    showinfo('Done','Copied to Clipboard')

'''
Name : password
purpose : to generate password of given length
'''
def password():
    global check1
    global check2
    global check3
    global f
    btn['state'] = DISABLED
    text = ''
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    lower = 'abcdefghijklmnopqrstuvwxyz' 
    num =  '0123456789' 
    special = '!@#$%^&*()_-=+/?\|][}{`~'
    x = int(ent.get())
    if var.get() == 1 and var1.get() == 1 and var2.get() == 1:
        for i in range(x):
            a = random.choice(upper)
            b = random.choice(lower)
            c = random.choice(num)
            d = random.choice(special)
            e = a + b + c + d
            text += e
        f = text[0:x]
        f1 = Frame(win,bg='black')
        f1.pack()
        lbl1 = Label(f1,text=f,bg='black',fg='orangered',font=('Roboto 16 bold italic'))
        lbl1.pack(side=LEFT)
        btn1 = Button(f1,text='Copy',command=addToClipboard,fg='black')
        btn1.pack(side=LEFT,padx=10)
    elif var.get() == 1 and var1.get() == 1:
        for i in range(x):
            a = random.choice(upper)
            b = random.choice(lower)
            c = random.choice(num)
            e = a + b + c
            text += e
        f = text[0:x]
        f1 = Frame(win,bg='black')
        f1.pack()
        lbl1 = Label(f1,text=f,bg='black',fg='orangered',font=('Roboto 16 bold italic'))
        lbl1.pack(side=LEFT)
        btn1 = Button(f1,text='Copy',command=addToClipboard,fg='black')
        btn1.pack(side=LEFT,padx=10)
    elif var.get() == 1 and var2.get() == 1:
        for i in range(x):
            a = random.choice(upper)
            b = random.choice(lower)
            c = random.choice(special)
            e = a + b + c
            text += e
        f = text[0:x]
        f1 = Frame(win,bg='black')
        f1.pack()
        lbl1 = Label(f1,text=f,bg='black',fg='orangered',font=('Roboto 16 bold italic'))
        lbl1.pack(side=LEFT)
        btn1 = Button(f1,text='Copy',command=addToClipboard,fg='black')
        btn1.pack(side=LEFT,padx=10)
    elif var1.get() == 1 and var2.get() == 1:
        for i in range(x):
            c = random.choice(num)
            d = random.choice(special)
            e = c + d 
            text += e
        f = text[0:x]
        f1 = Frame(win,bg='black')
        f1.pack()
        lbl1 = Label(f1,text=f,bg='black',fg='orangered',font=('Roboto 16 bold italic'))
        lbl1.pack(side=LEFT)
        btn1 = Button(f1,text='Copy',command=addToClipboard,fg='black')
        btn1.pack(side=LEFT,padx=10)
    elif var.get() == 1:
        for i in range(x):
            c = random.choice(upper)
            d = random.choice(lower)
            m = c+d
            text += d
        f = text[0:x]
        f1 = Frame(win,bg='black')
        f1.pack()
        lbl1 = Label(f1,text=f,bg='black',fg='orangered',font=('Roboto 16 bold italic'))
        lbl1.pack(side=LEFT)
        btn1 = Button(f1,text='Copy',command=addToClipboard,fg='black')
        btn1.pack(side=LEFT,padx=10)
       
    elif var1.get() == 1:
        for i in range(x):
            c = random.choice(num)
            text += c
        f = text[0:x]
        f1 = Frame(win,bg='black')
        f1.pack()
        lbl1 = Label(f1,text=f,bg='black',fg='orangered',font=('Roboto 16 bold italic'))
        lbl1.pack(side=LEFT)
        btn1 = Button(f1,text='Copy',command=addToClipboard,fg='black')
        btn1.pack(side=LEFT,padx=10)
    elif var2.get() == 1:
        for i in range(x):
            d = random.choice(special)
            text += d
        f = text[0:x]
        f1 = Frame(win,bg='black')
        f1.pack()
        '''Label in which the generated password will appear'''
        lbl1 = Label(f1,text=f,bg='black',fg='orangered',font=('Roboto 16 bold italic'))
        lbl1.pack(side=LEFT)
        '''Button with command to copy text to clipboard'''
        btn1 = Button(f1,text='Copy',command=addToClipboard,fg='black')
        btn1.pack(side=LEFT,padx=10)
    
'''Label'''    
lbl = Label(win,text='Password Generator',font=('Helvatica 20 bold italic'),fg='orangered',bg='black')
lbl.pack(fill=X)

'''Entry'''
ent = Entry(win,width=50,fg='green',font=('Roboto 10 bold italic'),relief='groove')
ent.insert(0,'Enter password length here...')
ent.bind('<FocusIn>',on_first_click)
ent.pack(pady=20,ipady=5)

'''whether checkbox is checked/unchecked'''
var = IntVar()
var1 = IntVar()
var2 = IntVar()

'''CheckButton'''
check1 = Checkbutton(win,text='Characters',variable=var)
check1.pack(ipadx=20)
check2 = Checkbutton(win,text='Numbers',variable=var1)
check2.pack(ipadx=23)
check3 = Checkbutton(win,text='Special Characters',variable=var2)
check3.pack()

'''Button with command to generate random password'''
btn = Button(win,text='Generate Password',bg='orangered',fg='white',relief='raised',command=password)
btn.pack(pady=15,ipady=10,ipadx=10)

win.mainloop()