from tkinter import *

class TutorialOne(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        global fontstyle
        fontstyle = ('calibri', 12)

        self.config(borderwidth='1', relief='solid')
        nextbtn = Button(self, text='next', command=self.gonext, font=fontstyle)
        nextbtn.place(relx=0.2, rely=0.95)

        global labelst
        labelst = Label(self, text='Hello and Welcome to CaPybara!\n\nIf you can read this, then it means you are ready '
                                   'to start learning Python. CaPybara will make that a bit easier for you.\n\nClick '
                                   '\'Next\' to start the tutorial.', justify='left', wraplength=290, anchor='center', font=fontstyle)
        labelst.place(relx=0, rely=0)


        self.pgno = 0



    def pageone(self):
        labelst.destroy()
        label = Label(self, text="Cool. Let's start it very simple.\n\nOn the left hand side of the main window, "
                                 "you should see a button that says 'Print message'.\n\nClick on it and once you are "
                                 "done, click 'next'.", justify='left', wraplength=290, anchor='center', font=fontstyle)
        label.place(relx=0, rely=0)



    def pagetwo(self):
        labelst.destroy()
        label = Label(self, text="CaPybara has written that code for you!"
                                 "\n\nAs you can tell, the following code will print whatever message you want it. Let's replace the placeholder text with \"Hello world\" (Don't forget the quotation marks!)."
                                 "\n\nOnce you're done, click on 'Run' at the top of the window.", justify='left', wraplength=290, anchor='center', font=fontstyle)
        label.place(relx=0, rely=0)
        self.pgno = 1



    def pagethree(self):
        labelst.destroy()
        label = Label(self, text="You should be able to see 'Hello world!' in the output window."
                                 "\n\nIf you can, great! You just created your first program in Python!"
                                 "\n\nIf you can't try to click 'back' and see if you missed any steps. Click on 'Finish' to complete this tutorial", justify='left', wraplength=290, anchor='center', font=fontstyle)
        label.place(relx=0, rely=0)

    def gonext(self):
        if self.pgno==3:
           self.destroy()
        if self.pgno == 2:
            self.pagethree()
            self.pgno = 3
            return 'break'
        if self.pgno == 1:
            self.pagetwo()
            self.pgno = 2
            return 'break'
        else:
            self.pageone()
            self.pgno = 1
            return 'break'



