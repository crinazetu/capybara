import os

from tkinter import *
from tkinter import ttk
import sandbox


class TutorialTwo(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        global fontstyle
        fontstyle = ('calibri', 12)

        self.config(borderwidth='1', relief='solid')
        nextbtn = ttk.Button(self, text='next', command=self.gonext)
        nextbtn.place(relx=0.5, rely=0.9, anchor='center')

        global labelst
        labelst = ttk.Label(self, text="Let's look into declaring and assigning variables."
                                       "\n\nThink of a variable as a little box where you put stuff in. the name if "
                                       "the variable is the box and its value is the thing that is inside of it. "
                                       "\n\nLet's start by storing this \"Hello world\" message into a variable."
                                       "\n\nOn the left hand side of the screen, click on \"set variable to...\".",
                            justify='left', wraplength=290, anchor='center', font=fontstyle)
        labelst.place(relx=0, rely=0)

        self.pgno = 0
        sandbox.textarea.insert(END, 'print(\"Hello World!\")')

    def pageone(self):
        labelst.destroy()
        label = ttk.Label(self, text="Nice, now change 'var' into \"message\" and \"val\" into \"Hello world!\"",
                          justify='left', wraplength=290, anchor='center', font=fontstyle)
        label.place(relx=0, rely=0)

    def pagetwo(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="You're almost there. Now change the \"hello world\" inside of the \"print\" line to "
                               "be just \"message\".\n\nYou don't need the quotation marks this time, as Python will "
                               "know what you are referring to.", justify='left', wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def pagethree(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="Oops! It seems that the variable has been declared after it's being used. Python is "
                               "an interpreted language, so any variable must be declared and assigned before "
                               "everything else. Move your new variable to the top, and try again", justify='left',
                          wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def pagefour(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="Congrats! Now you know how to use variables! You may close this tutorial now.",
                          justify='left', wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def checkforresult(self):
        global codetoread
        global outputtoread
        codetoread = sandbox.textarea.get(1.0, END)
        outputtoread = sandbox.outputarea.get(1.0, END)
        codewords = codetoread.splitlines()
        printindex = codewords.index("print(message)")
        varindex = codewords.index("message = \"Hello World!\"")
        if (printindex>varindex):
            return True
        else:
            return False


    def gonext(self):
        if self.pgno == 4:
            self.destroy()
        if self.pgno == 3:
            if self.checkforresult() and ('hello world' in outputtoread.lower()):
                self.pgno = 4
            else:
                print('Complete the task first!')
        if self.pgno == 2:
            #self.destroy()
            print(self.checkforresult())
            if (self.checkforresult()):
                self.pgno = 4
            else:
                self.pgno = 3
            return 'break'
        if self.pgno == 1:
            if ('<var> = <newValue>' in codetoread):
                self.pagetwo()
                self.pgno = 2
                return 'break'
            else:
                print('Complete the task first!')
        else:
            self.pageone()
            self.pgno = 1
            return 'break'
