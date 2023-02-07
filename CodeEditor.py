import idlelib.colorizer as ic
import idlelib.percolator as ip
import time
import re
import tkinter as tk
from LineNumbers import *



def setTextBox(parent, font_size, scrollbar):

    textarea = tk.Text(parent, font=('courier', font_size, 'bold'), yscrollcommand=scrollbar.set)
    t = Tool()
    textarea.bind("<Return>", lambda event, textw=textarea: t.indentLines(textw))
    ip.Percolator(textarea).insertfilter(ic.ColorDelegator())
    lines = LineNumbers(parent, textarea, width=2)
    lines.pack(side=tk.LEFT, fill=tk.BOTH)

    return textarea


class Tool:
    def indentLines(self, textw):
        text = textw.get(1.0, END)
        lines = text.splitlines()
        if lines[-1].endswith(':'):
            if lines[-1].startswith('\t'):
                textw.insert(END, '\n\t\t')
            else:
                textw.insert(END, '\n\t')
            return 'break'

        if lines[-1].startswith('\t\t\t'):
            print('triple tab')
            textw.insert(END, '\n\t\t\t')
            return 'break'

        if lines[-1].startswith('\t\t'):
            print('double tab')
            textw.insert(END, '\n\t\t')
            return 'break'

        if lines[-1].endswith('\t'):
            textw.insert(END, '\n\t')
            return 'break'


