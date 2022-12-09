import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
import subprocess
import os

import codeList
from codeList import *

path = ''
temppath = os.path.expanduser('~')
print(temppath)

def setup(frame, font_size):
    global sandboxFrame
    sandboxFrame = Frame(frame, bg='lightblue')
    global codeL
    codeL = codeList.createGUI(sandboxFrame)
    global scrollbar2
    scrollbar2 = Scrollbar(codeL, orient=VERTICAL)
    global editFrame
    editFrame = Frame(sandboxFrame, bg='white')
    global scrollbar
    scrollbar = Scrollbar(editFrame, orient=VERTICAL)
    global textarea
    textarea = Text(editFrame, font=('courier', font_size, 'bold'), yscrollcommand=scrollbar.set)
    global outputFrame
    outputFrame = LabelFrame(sandboxFrame, text='Console', font=('courier', 12, 'bold'))
    global visualOutputFrame
    visualOutputFrame = LabelFrame(sandboxFrame, text='Output', font=('courier', 12, 'bold'))
    global scrollbar1
    scrollbar1 = Scrollbar(outputFrame, orient=VERTICAL)
    global outputarea
    outputarea = Text(outputFrame, font=('courier', font_size, 'bold'), yscrollcommand=scrollbar1.set)



def font_inc(event=None):
    global font_size
    font_size += 1
    textarea.config(font=('courier', font_size, 'bold'))


def font_dec(event=None):
    global font_size
    font_size -= 1
    textarea.config(font=('courier', font_size, 'bold'))


def run_code():
    global path
    if path == '':
        newpath = temppath + '\\tempfile.py'
        file = open(newpath, 'x')
        file.write(textarea.get(1.0, END))
        file.close()
        command = f'python {newpath}'
        run_file = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = run_file.communicate()
        outputarea.delete(1.0, END)
        outputarea.insert(1.0, output)
        outputarea.insert(1.0, error)
        os.remove(newpath)
    if path != '':
        command = f'python {path}'
        run_file = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = run_file.communicate()
        outputarea.delete(1.0, END)
        outputarea.insert(1.0, output)
        outputarea.insert(1.0, error)


def saveas(event=None):
    global path
    path = filedialog.asksaveasfilename(filetypes=[('Python Files', '*.py')], defaultextension='.py')
    if path != '':
        file = open(path, 'w')
        file.write(textarea.get(1.0, END))
        file.close()


def openfile(event=None):
    global path
    print(os.getlogin())
    path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')], defaultextension='.py')
    print(path)
    if path != '':
        file = open(path, 'r')
        data = file.read()
        textarea.delete(1.0, END)
        textarea.insert(1.0, data)
        file.close()


def save(event=None):
    if path == '':
        saveas()
    else:
        file = open(path, 'w')
        file.write(textarea.get(1.0, END))
        file.close()


def new(event=None):
    global path
    path = ''
    textarea.delete(1.0, END)
    outputarea.delete(1.0, END)




def clear():
    textarea.delete(1.0, END)
    outputarea.delete(1.0, END)







def placeEverything(frame, fontsize):
    setup(frame, fontsize)
    sandboxFrame.place(x=0, y=0, width=1270, height=720)
    codeL.place(x=0, y=0, relwidth=0.1, relheight=1)
    scrollbar2.pack(side=RIGHT, fill=Y)
    editFrame.place(relx=0.1, y=0, relheight=0.8, relwidth=0.4)
    scrollbar.pack(side=RIGHT, fill=Y)
    textarea.pack(fill=BOTH)
    scrollbar.config(command=textarea.yview)
    outputFrame.place(relx=0.1, rely=0.8, relwidth=0.4, relheight=0.2)
    visualOutputFrame.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
    scrollbar1.pack(side=RIGHT, fill=Y)
    outputarea.pack(fill=BOTH)
    scrollbar1.config(command=textarea.yview)
