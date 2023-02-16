# This script puts everything together into one runnable program.
# Mainly focuses on GUI and allowing you to go from page to page
# Also contains some universal functions that will work regardless of what page you're in

import tkinter as tk
from tkinter import ttk

import sandbox
from sandbox import *
import NewWindow

from ttkthemes import ThemedTk

directory = 'CaPybara projects'
dirpath = os.path.join(temppath, directory)
if os.path.exists(dirpath):
    pass
else:
    os.mkdir(dirpath)
    print("Directory '% s' created" % directory)

# Set up root, the main window
root = ThemedTk(theme='adapta')
root.geometry('1000x760+0+0')
root.title('CaPybara')

global font_size
font_size = 12

# Checkmark for one of the drop-down lists
global check
check = tk.StringVar()
# Sets up toolbar on the top of the window

# Sets up file menu in the toolbar
global filemenu
filemenu = ttk.Frame(root)
filemenu.place(x=0, y=0, relwidth=1, height=40)

# Universal frame, this will hold in every page
global uniFrame
uniFrame = ttk.Frame(root)
uniFrame.place(x=0, y=40, width=1000, height=720)

# iexit exits the application
def iexit(event=None):
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def course():
    nw = NewWindow.NewWindow('title',root)
    nw.tutorial()

def about():
    NewWindow.NewWindow('title', root).aboutPage()

# sets buttons up within the top menu with their corresponding functions.
nficon = PhotoImage(file= r"Sprites\new_file.png")
nf = ttk.Button(filemenu, image=nficon, command=new)
nf.place(x=0,y=0)
oficon = PhotoImage(file=r"Sprites\open_file.png")
of = ttk.Button(filemenu, image=oficon, command=openfile)
of.place(x=55, y=0)
svicon = PhotoImage(file=r"Sprites\save.png")
sv = ttk.Button(filemenu, image=svicon, command=save)
sv.place(x=(55*2), y=0)
svaicon= PhotoImage(file="Sprites\save_as.png")
sva = ttk.Button(filemenu, image=svaicon, command=saveas)
sva.place(x=(55*3), y=0)
clicon = PhotoImage(file=r"Sprites\clear.png")
cl = ttk.Button(filemenu, image=clicon, command=clear)
cl.place(x=(55*4), y=0)
rnicon = PhotoImage(file=r"Sprites\play.png")
rn= ttk.Button(filemenu, image=rnicon, command=run_code)
rn.place(x=(55*5), y=0)
tuticon = PhotoImage(file=r"Sprites\tutorial.png")
tut = ttk.Button(filemenu, image=tuticon, command=course)
tut.place(x=(55*6), y=0)
infoicon = PhotoImage(file=r"Sprites\info.png")
info = ttk.Button(filemenu, image=infoicon, command=about)
info.place(x=(1000-55), y=0)

# Page containing sandbox
def sandboxPage(uniFrame):
    sandbox.placeEverything(uniFrame, font_size)


#root.config(menu=myMenu)

root.bind('<Control-n>',new)
root.bind('<Control-o>',openfile)
root.bind('<Control-s>',save)
root.bind('<Control-a>',saveas)
root.bind('<Control-p>',font_inc)
root.bind('<Control-m>',font_dec)

img = PhotoImage(file='Sprites/capybaraiconsm.png')
root.wm_iconphoto(True, img)

sandboxPage(uniFrame)
w = NewWindow.NewWindow('title',root)
ww = w.welcomePage()
root.mainloop()