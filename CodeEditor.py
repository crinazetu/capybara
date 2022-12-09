import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
import tkinter as tk
from LineNumbers import *


def setTextBox(parent, font_size, scrollbar):
   textarea = tk.Text(parent, font=('courier', font_size, 'bold'), yscrollcommand=scrollbar.set)
   ip.Percolator(textarea).insertfilter(ic.ColorDelegator())
   lines = LineNumbers(parent, textarea, width=2)
   lines.pack(side=tk.LEFT, fill=tk.BOTH)
   return textarea

