from tkinter import *
from tkinter import filedialog, messagebox



class CodeButton():
    def __init__(self, name, codetext):
        self.name = name
        self.codetext = codetext

    def getName(self):
        return self.name

    def getCode(self):
        return self.codetext
