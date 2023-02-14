import subprocess
import os

import codeList
from codeList import *
import CodeEditor

from tkinter import ttk


path = ''
temppath = os.path.expanduser('~')
#directory = 'CaPybara projects'
#dirpath = os.path.join(temppath, directory)
#print(temppath)


def setup(frame, font_size):
    global sandboxFrame
    sandboxFrame = ttk.Frame(frame)
    # global codeL
    # codeL = codeList.createGUI(sandboxFrame)

    global editFrame
    editFrame = ttk.Frame(sandboxFrame)
    global scrollbar
    scrollbar = ttk.Scrollbar(editFrame, orient=VERTICAL)
    global textarea
    textarea = CodeEditor.setTextBox(editFrame, font_size, scrollbar)
    global outputFrame
    outputFrame = ttk.LabelFrame(sandboxFrame, text='Console')
    global scrollbar1
    scrollbar1 = ttk.Scrollbar(outputFrame, orient=VERTICAL)
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
    sandboxFrame.place(x=0, y=0, width=1000, height=720)
    codeList.createGUI(frame)
    # scrollbar2.config(side=RIGHT, fill=Y)
    editFrame.place(relx=0.2, y=0, relheight=0.8, relwidth=0.8)
    # scrollbar.config(side=RIGHT, fill=Y)

    textarea.pack(fill=BOTH)
    scrollbar.config(command=textarea.yview)
    outputFrame.place(relx=0.2, rely=0.8, relwidth=0.8, relheight=0.2)

    scrollbar1.pack(side=RIGHT, fill=Y)
    outputarea.pack(fill=BOTH)
    scrollbar1.config(command=textarea.yview)
