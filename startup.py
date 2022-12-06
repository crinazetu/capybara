import tkinter as tk
from tkinter import messagebox

import sandbox
from sandbox import *

root = tk.Tk()
root.geometry('1270x670+0+0')
root.title('CaPybara')
global font_size
font_size = 15

global check
check = tk.StringVar()
global myMenu
myMenu = tk.Menu()
global filemenu
filemenu = tk.Menu(myMenu, tearoff=False)
global thememenu
thememenu = tk.Menu(myMenu, tearoff=False)
global uniFrame
uniFrame = tk.Frame(root)
uniFrame.place(x=0, y=0, width=1270, height=720)

def iexit(event=None):
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def theme():
    if check.get() == 'light':
        sandbox.textarea.config(bg='white', fg='black')
        sandbox.outputarea.config(bg='white', fg='black')

    if check.get() == 'dark':
        sandbox.textarea.config(bg='gray20', fg='white')
        sandbox.outputarea.config(bg='gray20', fg='white')

filemenu.add_command(label='New File',accelerator='Ctrl+N',command=new)
filemenu.add_command(label='Open File',accelerator='Ctrl+O',command=openfile)
filemenu.add_command(label='Save',accelerator='Ctrl+S',command=save)
filemenu.add_command(label='Save as',accelerator='Ctrl+A',command=saveas)
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',command=iexit)
myMenu.add_cascade(label='File',menu=filemenu)


thememenu.add_radiobutton(label='Light',variable=check,value='light',command=theme)
thememenu.add_radiobutton(label='Dark',variable=check,value='dark',command=theme)

myMenu.add_cascade(label='Themes',menu=thememenu)

myMenu.add_command(label='Clear',command=clear)

myMenu.add_command(label='Run',command=run_code)
check.set('light')


def page1(uniFrame):
    page = tk.Frame(uniFrame, bg='#55f0f2')
    page.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Button(page, text='Start', command=changepage).place(relx=0.5, rely=0.5)


def page2(uniFrame):
    sandbox.placeEverything(uniFrame, font_size)

def changepage():
    global pagenum, root
    for widget in root.winfo_children():
        if root.winfo_children().__contains__(myMenu):
            continue
        else:
            widget.destroy()
    if pagenum == 1:
        page2(root)
        pagenum = 2
    else:
        page1(root)
        pagenum = 1

pagenum = 1


root.config(menu=myMenu)

root.bind('<Control-n>',new)
root.bind('<Control-o>',openfile)
root.bind('<Control-s>',save)
root.bind('<Control-a>',saveas)
root.bind('<Control-q>',iexit)
root.bind('<Control-p>',font_inc)
root.bind('<Control-m>',font_dec)

page1(uniFrame)
root.mainloop()