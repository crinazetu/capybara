from tkinter import *
import TutorialOne
import TutorialTwo
from tkinter import ttk

class NewWindow(Toplevel):

    def __init__(self, titled, label, master=None):
        super().__init__(master=master)
        self.title(titled)
        self.geometry("300x500")
        label = ttk.Label(self, text=label)
        label.pack()

    def tutorial(self):
        global unipage
        unipage = ttk.Frame(self)
        unipage.place(x=0, y=0, relwidth=1, relheight=1)

        global tutorialonebtn
        tutorialonebtn = ttk.Button(unipage, text='Getting started', command=self.tutone, width=42)
        tutorialonebtn.grid(row=0, column=0)
        global tutorialtwobtn
        tutorialtwobtn = ttk.Button(unipage, text='Looking into variables', command=self.tuttwo, width=42)
        tutorialtwobtn.grid(row=1, column=0)


    def tutone(self):
        TutorialOne.TutorialOne(master=unipage).place(relx=0, rely=0, relheight=1, relwidth=1)

    def tuttwo(self):
        TutorialTwo.TutorialTwo(master=unipage).place(relx=0, rely=0, relheight=1, relwidth=1)



