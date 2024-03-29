import tkinter

import sandbox
from CodeButton import *
from tkinter import ttk
import createCodeList
from CollapsablePane import CollapsiblePane as cp


def createGUI(parentframe):
    frame_main = ttk.Frame(parentframe)
    frame_main.grid(sticky='news')
    frame_canvas = ttk.Frame(frame_main)
    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    frame_canvas.grid_propagate(False)

    # Add a canvas in that frame
    canvas = Canvas(frame_canvas, bg="lightblue")
    canvas.grid(row=0, column=0, sticky="news")

    vsb = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    frame_buttons = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

    list = createCodeList.createList(frame_buttons)
    columns = len(list)
    for j in range(columns):
        list[j].grid(row=j, column=0, sticky='news')
        list[j].config(width=27)

    frame_buttons.update_idletasks()
    frame_canvas.config(width=185 + vsb.winfo_width(),
                       height=720)

    canvas.config(scrollregion=canvas.bbox("all"))


