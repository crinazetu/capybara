from tkinter import *
import TutorialOne

class NewWindow(Toplevel):

    def __init__(self, titled, label, master=None):
        super().__init__(master=master)
        self.title(titled)
        self.geometry("300x720")
        label = Label(self, text=label)
        label.pack()

    def tutorial(self):
        global unipage
        unipage = Frame(self)
        unipage.place(x=0, y=0, relwidth=1, relheight=1)

        global tutorialonebtn
        tutorialonebtn = Button(unipage, text='Start Tutorial One', command=self.startpage, width=40)
        tutorialonebtn.grid(row=0, column=0)
        global startbtn
        startbtn = Button(unipage, text="start", command=self.startpage)
        startbtn.place(relx=0.2, rely=0.95)


    def startpage(self):
        TutorialOne.TutorialOne(master=unipage).place(relx=0, rely=0, relheight=1, relwidth=1)
        startbtn.destroy()


