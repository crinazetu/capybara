from tkinter import *


class NewWindow(Toplevel):

    def __init__(self, titled, size, label, master=None):
        super().__init__(master=master)
        self.title(titled)
        self.geometry(size)
        label = Label(self, text=label)
        label.pack()

    def tutorial(self):
        unipage = Frame(self, bg='blue')
        unipage.place(x=0, y=0, relwidth=1, relheight=1)

        stepone = Frame(unipage, bg='lightblue')
        stepone.place(relx=0.025, rely=0.025,relwidth=0.95, relheight=0.95)
        global pagenum_tutorial
        pagenum_tutorial = 1

        nextbtn = Button(unipage, text="next", command=self.changepagetut)
        nextbtn.place(relx=0, rely=0.95)

    def changepagetut(self):
        print("should change the page")

