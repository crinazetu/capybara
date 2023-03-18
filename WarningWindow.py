from tkinter import *


class WarningWindow(Toplevel):

    def __init__(self, titled, master=None):
        super().__init__(master=master)
        self.title(titled)
        self.geometry("200x90")
        Label(self, text="Complete the task first!").place(relx=0.1, rely=0.1)
        Button(self, text="OK", command=self.close).place(relx=0.45, rely=0.6)

    def close(self):
        self.destroy()