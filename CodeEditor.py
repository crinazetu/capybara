import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
import tkinter as tk
from LineNumbers import *


global textarea

def setTextBox(parent, font_size, scrollbar):

    textarea = tk.Text(parent, font=('courier', font_size, 'bold'), yscrollcommand=scrollbar.set)
    t = Tool()
    textarea.bind("<Return>", lambda textw=textarea: t.indentLines(textw))
    ip.Percolator(textarea).insertfilter(ic.ColorDelegator())
    lines = LineNumbers(parent, textarea, width=2)
    lines.pack(side=tk.LEFT, fill=tk.BOTH)

    return textarea


class Tool:
    def indentLines(self, textw):
        text = textw.get(1.0, END)
        lines = text.split('\n')
        if lines[-1].endswith(':'):
            textw.insert(END, '\t')

