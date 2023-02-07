from tkinter import *
from tkinter.ttk import *


class NewWindow(Toplevel):

    def __init__(self, titled, size, label, master=None):
        super().__init__(master=master)
        self.title(titled)
        self.geometry(size)
        label = Label(self, text=label)
        label.pack()
