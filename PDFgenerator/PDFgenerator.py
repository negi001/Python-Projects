# importing modules
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
from fpdf import FPDF

# global empty list
image_list = []

def add_img():
    n = int(ent1.get())
    for i in range(n):
        image = askopenfilename(defaultextension=".png",
        filetypes=[("All Files","*.*")])
        image_list.append(image)

def convert():
    pdf = FPDF()
    a = asksaveasfilename(initialfile="Untitled.pdf",
            defaultextension=".pdf",filetypes=[("All Files","*.*")])
    for image in image_list:
        pdf.add_page()
        pdf.image(image,x=None,y=None,w=100,h=100)
    pdf.output(a,"F")
    showinfo("Done","File is saved !")

firstclick = True

def on_entry_click(event):
    global firstclick
    if firstclick:
        firstclick = False
        ent1.delete(0,"end")            

win = Tk()
win.title('Image to PDF Convertor')
win.geometry('400x400')
win.configure(bg="yellow")
win.resizable(0,0)

my_font = Font(family=("TimesNewRoman 20 bold italic"),underline=1)
lbl = Label(win,text="PDF CONVERTOR",font=my_font,bg="yellow",fg="red")
lbl.pack(pady=5)

ent1 = Entry(win,width=40,relief="solid",font=("Helvatica 12 italic"))
ent1.insert(0, "Enter number of images to convert ...")
ent1.bind('<FocusIn>',on_entry_click)
ent1.pack(pady=8,ipady=3)

btn = Button(win,text="Add Image",relief="ridge",command=add_img)
btn.pack(pady=10,ipadx=40)

btn2 = Button(win,text="Convert to PDF",relief="ridge",command=convert)
btn2.pack(ipadx=35)

win.mainloop()
