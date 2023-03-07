from tkinter import *
from tkinter import ttk
import sandbox


class TutorialThree(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)


        global fontstyle
        fontstyle = ('calibri', 12)

        self.config(borderwidth='1', relief='solid')
        nextbtn = ttk.Button(self, text='next', command=self.gonext)
        nextbtn.place(relx=0.5, rely=0.9, anchor='center')

        global labelst
        labelst = ttk.Label(self, text="Today we are going to look into how loops work. The following code should "
                                       "print 'hello world' 5 times. Run it to give it a try, then proceed to the "
                                       "next step.",
                            justify='left', wraplength=290, anchor='center', font=fontstyle)
        labelst.place(relx=0, rely=0)

        self.pgno = 0
        sandbox.textarea.insert(END, 'print(\"Hello World!\")\nprint(\"Hello World!\")\nprint(\"Hello '
                                     'World!\")\nprint(\"Hello World!\")\nprint(\"Hello World!\")\n')

    def pageone(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="The code runs just fine, but it's a bit clunky. Python has a more elegant way of "
                               "running the same commands multiple times using loops. Let’s start by inserting a 'for "
                               "loop' from your command window at the left of your window.", justify='left',
                          wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def pagetwo(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="\'in range\' here refers to how many times you want something to happen. If we want "
                               "the code inside of the loop to run 5 times, replace the x with 5", justify='left',
                          wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def pagethree(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="Delete all of the print lines so that there is only one left. Then, move this line so "
                               "it is inside of the loop, so that it replaces 'command'. There should be no code "
                               "outside of the loop",
                          justify='left', wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def pagefour(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="Everything looks good. Let's give the code a run!",
                          justify='left', wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def pagefive(self):
        labelst.destroy()
        label = ttk.Label(self,
                          text="Congratulations! Now you know how to use loops in Python!",
                          justify='left', wraplength=290, anchor='center',
                          font=fontstyle)
        label.place(relx=0, rely=0)

    def gonext(self):
        codetoread = sandbox.textarea.get(1.0, END)
        outputtoread = sandbox.outputarea.get(1.0, END)

        if self.pgno == 5:
            self.destroy()
        if self.pgno == 4:
            if "for x in range (5):\n\tprint(\"Hello World!\")" in codetoread and "Hello world!" in outputtoread:
                self.pagefive()
                self.pgno = 5
                return 'break'
            else:
                print('Complete the task first!')
        if self.pgno == 3:
            if "for x in range (5):\n\tprint(\"Hello World!\")" in codetoread:
                self.pagefour()
                self.pgno = 4
                return 'break'
            else:
                print('Complete the task first!')
        if self.pgno == 2:
            if "for x in range (5):\n\t(insert code)" in codetoread:
                self.pagethree()
                self.pgno = 3
                return 'break'
            else:
                print('Complete the task first!')
        if self.pgno == 1:
            if "for x in range (insert):\n\t(insert code)" in codetoread:
                self.pagetwo()
                self.pgno = 2
                return 'break'
            else:
                print('Complete the task first!')
        else:
            if "Hello world!" in outputtoread:
                self.pageone()
                self.pgno = 1
                return 'break'
            else:
                print('Complete the task first!')