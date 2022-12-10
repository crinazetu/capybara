# This script puts everything together into one runnable program.
# Mainly focuses on GUI and allowing you to go from page to page
# Also contains some universal functions that will work regardless of what page you're in

import tkinter as tk
from tkinter import messagebox
import sandbox
from sandbox import *

# Set up root, the main window
root = tk.Tk()
root.geometry('1270x720+0+0')
root.title('CaPybara')

global font_size
font_size = 15

# Checkmark for one of the drop-down lists
global check
check = tk.StringVar()
# Sets up toolbar on the top of the window
global myMenu
myMenu = tk.Menu()
# Sets up file menu in the toolbar
global filemenu
filemenu = tk.Menu(myMenu, tearoff=False)

# Universal frame, this will hold in every page
global uniFrame
uniFrame = tk.Frame(root)
uniFrame.place(x=0, y=0, width=1270, height=720)

# iexit exits the application
def iexit(event=None):
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

# sets buttons up within the top menu with their corresponding functions.
filemenu.add_command(label='New File',accelerator='Ctrl+N',command=new)
filemenu.add_command(label='Open File',accelerator='Ctrl+O',command=openfile)
filemenu.add_command(label='Save',accelerator='Ctrl+S',command=save)
filemenu.add_command(label='Save as',accelerator='Ctrl+A',command=saveas)
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',command=iexit)
myMenu.add_cascade(label='File',menu=filemenu)


myMenu.add_command(label='Clear',command=clear)

myMenu.add_command(label='Run',command=run_code)
check.set('light')

# PAGE 1
# The first page you see when you open the application
def startPage(uniFrame):
    page = tk.Frame(uniFrame, bg='#55f0f2')
    page.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Button(page, text='Start', command=changepage).place(relx=0.5, rely=0.5)

# PAGE 2
# Page containing sandbox
def sandboxPage(uniFrame):
    sandbox.placeEverything(uniFrame, font_size)

# changepage makes it possible to change the contents of the universal frame
def changepage():
    global pagenum, root
    for widget in root.winfo_children():
        # makes sure the manu is present regardless of what page you're on
        if root.winfo_children().__contains__(myMenu):
            continue
        else:
            widget.destroy()
    if pagenum == 1:
        sandboxPage(root)
        pagenum = 2
    else:
        startPage(root)
        pagenum = 1

pagenum = 2


root.config(menu=myMenu)

root.bind('<Control-n>',new)
root.bind('<Control-o>',openfile)
root.bind('<Control-s>',save)
root.bind('<Control-a>',saveas)
root.bind('<Control-q>',iexit)
root.bind('<Control-p>',font_inc)
root.bind('<Control-m>',font_dec)

sandboxPage(uniFrame)
root.mainloop()