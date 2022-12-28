import tkinter as tk
import turtle
from CodeButton import *
import codeList
import CollapsablePane


def setupCanvas(visualOutputFrame):
    canvas = tk.Canvas(visualOutputFrame, width=550, height=450, bd=1, relief='solid')
    global t
    t = turtle.RawTurtle(canvas=canvas)
    return canvas

def placeCanvas(canvas):
    canvas.place(anchor='center', relx=0.5, rely=0.35)

def writeSomething():
    t.fd(50)