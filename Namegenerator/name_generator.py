import os
import names
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror, showinfo

win = Tk()
win.title('Name Generator')
win.geometry('450x360')
win.resizable(0,0)
win.configure(bg='crimson')

def addToClipboard():
    global f_name
    command = 'echo | set /p nul=' + f_name+' '+str(ent1.get()).strip() + '| clip'
    os.system(command)
    showinfo('Done','Copied to Clipboard')

def genName():
	global lxl
	global lzl
	global f_name
	global bzn
	# conditons
	if ent.get() == '' or ent2.get() == '' or ent3.get() == '' or ent4.get() == '':
		showerror('Error', 'All fields are neccessary to be filled')
	# elif str(ent.get()) == 'male' or str(ent.get()) == 'female':
	# 	pass
	elif int(ent2.get()) > 31 or int(ent3.get()) > 12 or int(ent4.get()) < 2020:
		showerror('Error','Invalid Date Input')
	elif str(ent1.get()) == '':
		fz = Frame(win,bg='crimson')
		fz.pack()
		f_name = names.get_full_name(gender=str(ent.get()).lower())
		lzl = Label(fz,text=f_name,bg='crimson',fg='white',font=('Roboto 18 bold'))
		lzl.pack(pady=10,side=LEFT)
		bzn = Button(fz,text='+',command=addToClipboard)
		bzn.pack(side=LEFT,padx=10,ipadx=10)
	elif str(ent1.get()) != '':
		fz = Frame(win,bg='crimson')
		fz.pack()
		f_name = names.get_first_name(gender=str(ent.get()))
		lzl = Label(fz,text=f_name+' '+str(ent1.get()),bg='crimson',fg='white',font=('Roboto 18 bold'))
		lzl.pack(side=LEFT,pady=10)
		bzn = Button(fz,text='+',command=addToClipboard)
		bzn.pack(side=LEFT,padx=10,ipadx=10)
	# else:
	# 	showerror('Error','Invalid Gender Input')
	btn['state'] = DISABLED


def clear():
	global lzl
	global bzn
	ent.delete(0,'end')
	ent1.delete(0,'end')
	ent2.delete(0,'end')
	ent3.delete(0,'end')
	ent4.delete(0,'end')
	btn['state'] = NORMAL
	lzl.destroy()
	bzn.destroy()


firstclick = True

def on_first_click(event):
	global firstclick
	if firstclick:
		firstclick = False
		ent.delete(0,'end')

secondclick = True

def on_second_click(event):
	global secondclick
	if secondclick:
		secondclick = False
		ent1.delete(0,'end')


thirdclick = True

def on_third_click(event):
	global thirdclick
	if thirdclick:
		thirdclick = False
		ent2.delete(0,'end')

fourthclick = True

def on_fourth_click(event):
	global fourthclick
	if fourthclick:
		fourthclick = False
		ent3.delete(0,'end')


fifthclick = True

def on_fifth_click(event):
	global fifthclick
	if fifthclick:
		fifthclick = False
		ent4.delete(0,'end')


lbl = Label(win,text='NAME GENERATOR',bg='yellow',fg='red',font=('Roboto 18 bold'))
lbl.pack(fill=X)

f = Frame(win,bg='crimson')
f.pack(pady=15)

lbl = Label(f,text='Gender : ',bg='crimson',fg='white',font=('Roboto 14 bold'))
lbl.pack(side=LEFT)
ent = Entry(f,width=30,relief='solid')
ent.insert(0,'Male or Female...')
ent.bind('<FocusIn>',on_first_click)
ent.pack(side=LEFT,padx=5,ipady=5)

f2 = Frame(win,bg='crimson')
f2.pack(pady=10)

lbl1 = Label(f2,text='SURNAME : ',bg='crimson',fg='white',font=('Roboto 14 bold'))
lbl1.pack(side=LEFT)
ent1 = Entry(f2,width=30,relief='solid')
ent1.insert(0,'Enter the surname...')
ent1.bind('<FocusIn>',on_second_click)
ent1.pack(side=LEFT,padx=5,ipady=5)

f1 = Frame(win,bg='crimson')
f1.pack(pady=10)

lbl1 = Label(f1,text='DOB : ',bg='crimson',fg='white',font=('Roboto 14 bold'))
lbl1.pack(side=LEFT)
ent2 = Entry(f1,width=10,relief='solid')
ent2.insert(0,'DD')
ent2.bind('<FocusIn>',on_third_click)
ent2.pack(side=LEFT,padx=5,ipady=5)
ent3 = Entry(f1,width=10,relief='solid')
ent3.insert(0,'MM')
ent3.bind('<FocusIn>',on_fourth_click)
ent3.pack(side=LEFT,padx=5,ipady=5)
ent4 = Entry(f1,width=10,relief='solid')
ent4.insert(0,'YYYY')
ent4.bind('<FocusIn>',on_fifth_click)
ent4.pack(side=LEFT,padx=5,ipady=5)

btn = Button(win,text='Generate Name',bg='yellow',fg='red',font=('Roboto 10 bold'),command=genName)
btn.pack(ipady=5,pady=10)

btn2 = Button(win,text='Clear',bg='Blue',fg='white',font=('Roboto 10 bold'),command=clear)
btn2.pack(ipady=3,ipadx=25)

win.mainloop()
