from tkinter import *

import PIL
from PIL import ImageTk, Image

import TutorialOne
import TutorialTwo
import TutorialThree
from tkinter import ttk

class NewWindow(Toplevel):

    def __init__(self, titled, master=None):
        super().__init__(master=master)
        self.title(titled)

    def welcomePage(self):
        self.geometry("500x500")
        label = ttk.Label(self, text="Welcome to CaPybara!")
        label.pack()
        capybara = ImageTk.PhotoImage(Image.open(r"C:\Users\crina\PycharmProjects\CaPybara\Sprites\cpysmall.png"))
        img = Label(self, image=capybara)
        img.image = capybara
        img.place(x=250, y=250, anchor='center')

    def aboutPage(self):
        self.geometry("300x300")
        capybara = ImageTk.PhotoImage(Image.open(r"C:\Users\crina\PycharmProjects\CaPybara\Sprites\cpysmall.png").resize((233, 150)))
        img = Label(self, image=capybara)
        img.image = capybara
        img.place(x=150, y=100, anchor='center')
        desc = Label(self, text="CaPybara ver 1.0\nDeveloped by Crina Zetu (2022-2023)", justify=LEFT)
        desc.place(x=0, y=200)



    def tutorial(self):
        self.geometry("300x500")
        global unipage
        unipage = ttk.Frame(self)
        unipage.place(x=0, y=0, relwidth=1, relheight=1)

        global tutorialonebtn
        tutorialonebtn = ttk.Button(unipage, text='Getting started', command=self.tutone, width=42)
        tutorialonebtn.grid(row=0, column=0)
        global tutorialtwobtn
        tutorialtwobtn = ttk.Button(unipage, text='Looking into variables', command=self.tuttwo, width=42)
        tutorialtwobtn.grid(row=1, column=0)
        global tutorialthreebtn
        tutorialthreebtn = ttk.Button(unipage, text='Introducing loops', command=self.tutthree, width=42)
        tutorialthreebtn.grid(row=2, column=0)


    def tutone(self):
        TutorialOne.TutorialOne(master=unipage).place(relx=0, rely=0, relheight=1, relwidth=1)

    def tuttwo(self):
        TutorialTwo.TutorialTwo(master=unipage).place(relx=0, rely=0, relheight=1, relwidth=1)

    def tutthree(self):
        TutorialThree.TutorialThree(master=unipage).place(relx=0, rely=0, relheight=1, relwidth=1)




