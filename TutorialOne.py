from tkinter import *

class TutorialOne(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.config(borderwidth='1', relief='solid')
        nextbtn = Button(self, text='next', command=self.gonext)
        nextbtn.place(relx=0.2, rely=0.95)
        global labelst
        labelst = Label(self, text='Welcome to this starting tutorial')
        labelst.place(relx=0, rely=0)

    def pageone(self):
        labelst.destroy()
        label = Label(self, text="Welcome, this is step one")
        label.place(relx=0, rely=0)

    def gonext(self):
        self.pageone()