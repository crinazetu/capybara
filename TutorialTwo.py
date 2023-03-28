import os

from tkinter import *
from tkinter import ttk
import sandbox
import WarningWindow
import createCodeList


class TutorialTwo(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        global fontstyle
        fontstyle = ('calibri', 12)

        self.config(borderwidth='1', relief='solid')
        global nextbtn
        nextbtn = ttk.Button(self, text='next', command=self.gonext)
        nextbtn.place(relx=0.5, rely=0.9, anchor='center')

        global labelst
        labelst = ttk.Label(self, text="Let's look into declaring and assigning variables."
                                       "\n\nThink of a variable as a little box where you put stuff in. the name if "
                                       "the variable is the box and its value is the thing that is inside of it. "
                                       "\n\nLet's start by storing this \"Hello world\" message into a variable."
                                       "\n\nOn the left hand side of the screen, click on \"New Variable\".",
                            justify='left', wraplength=290, anchor='center', font=fontstyle, background='#f0f0ed')
        labelst.place(relx=0, rely=0)

        self.pgno = 0
        sandbox.textarea.delete(1.0, END)
        sandbox.textarea.insert(END, 'print(\"Hello World!\")')

    def pageone(self):
        labelst.destroy()
        label = ttk.Label(self, text="Nice, now change \'insert_variable_name\' into \"message\" and \'insert_value\' into \"Hello world!\"",
                          justify='left', wraplength=290, anchor='center', font=fontstyle, background='#f0f0ed')
        label.place(relx=0, rely=0)

    def pagetwo(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="You're almost there. Now change the \"hello world\" inside of the \"print\" line to "
                               "be just \"message\".\n\nYou don't need the quotation marks this time, as Python will "
                               "know what you are referring to.", justify='left', wraplength=290, anchor='center',
                          font=fontstyle, background='#f0f0ed')
        label.place(relx=0, rely=0)

    def pagethree(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="Oops! It seems that the variable has been declared after it's being used. Python is "
                               "an interpreted language, so any variable must be declared and assigned before "
                               "everything else. Move your new variable to the top, and try again", justify='left',
                          wraplength=290, anchor='center',
                          font=fontstyle, background='#f0f0ed')
        label.place(relx=0, rely=0)

    def pagefour(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="Congrats! Now you know how to use variables! You may close this tutorial now.",
                          justify='left', wraplength=295, anchor='center',
                          font=fontstyle, background='#f0f0ed')
        label.place(relx=0, rely=0)

    def checkforresult(self):

        codetoread = sandbox.textarea.get(1.0, END)
        outputtoread = sandbox.outputarea.get(1.0, END)
        codewords = codetoread.splitlines()
        printindex = codewords.index("print(message)")
        varindex = codewords.index("message = \"Hello World!\"")
        if (printindex>varindex):
            return True
        else:
            return False

    def clearContent(self):
        for widget in self.winfo_children():
            if widget != nextbtn:
                widget.destroy()


    def gonext(self):
        codetoread = sandbox.textarea.get(1.0, END)
        outputtoread = sandbox.outputarea.get(1.0, END)
        if self.pgno == 4:
            self.destroy()
        if self.pgno == 3:
            if self.checkforresult():
                self.clearContent()
                self.pagefour()
                self.pgno = 4
                return 'break'
            else:
                WarningWindow.WarningWindow("",self)
        if self.pgno == 2:
            if "print(message)" not in codetoread:
                WarningWindow.WarningWindow("",self)
            else:
                if self.checkforresult():
                    self.clearContent()
                    self.pagefour()
                    self.pgno = 4
                    return 'break'
                else:
                    self.clearContent()
                    self.pagethree()
                    self.pgno = 3
                    return 'break'
        if self.pgno == 1:
            if ('message = \'hello world!\'' in codetoread.lower() or 'message = \"hello world!\"' in codetoread.lower()):
                self.clearContent()
                self.pagetwo()
                self.pgno = 2
                return 'break'
            else:
                WarningWindow.WarningWindow("",self)
        else:
            if (createCodeList.variableIs.codetext in codetoread):
                self.pageone()
                self.pgno = 1
                return 'break'
            else:
                WarningWindow.WarningWindow("",self)

