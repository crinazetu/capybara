import os

from tkinter import *
import sandbox

class TutorialTwo(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        global fontstyle
        fontstyle = ('calibri', 12)

        self.config(borderwidth='1', relief='solid')
        nextbtn = Button(self, text='next', command=self.gonext, font=fontstyle)
        nextbtn.place(relx=0.5, rely=0.9, anchor='center')

        global labelst
        labelst = Label(self, text="Let's look into declaring and assigning variables."
                                   "\n\nThink of a variable as a little box where you put stuff in. the name if the variable is the box and its value is the thing that is inside of it."
                                   "\n\nLet's start by storing this \"Hello world\" message into a variable."
                                   "\n\nOn the left hand side of the screen, click on \"set variable\".", justify='left', wraplength=290, anchor='center', font=fontstyle)
        labelst.place(relx=0, rely=0)

        self.pgno = 0
        sandbox.textarea.insert(END, 'print(\"Hello World!\")')



    def pageone(self):
        labelst.destroy()
        label = Label(self, text="Nice, now change 'var' into \"message\" and \"val\" into \"Hello world!\"", justify='left', wraplength=290, anchor='center', font=fontstyle)
        label.place(relx=0, rely=0)


    def pagetwo(self):
        labelst.destroy()
        label = Label(self, text="You're almost there. Now change the \"hello world\" inside of the \"print\" line to "
                                 "be just \"message\".\n\nYou don't need the quotation marks this time, as Python will "
                                 "know what you are referring to.", justify='left', wraplength=290, anchor='center',
                      font=fontstyle)
        label.place(relx=0, rely=0)

    def gonext(self):
        if self.pgno==2:
           self.destroy()
      #  if self.pgno == 2:
       #     self.pagethree()
       #     self.pgno = 3
       #     return 'break'
        if self.pgno == 1:
            self.pagetwo()
            self.pgno = 2
            return 'break'
        else:
            self.pageone()
            self.pgno = 1
            return 'break'



