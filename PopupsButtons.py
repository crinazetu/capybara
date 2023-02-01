from tkinter import *
import time

class PopupsButtons(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def show(self, codetext, text):
        self.text = text

        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_pointerx()
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        canvas = Frame(tw)
        canvas.grid(row=2, column=0)
        codelabel= Label(canvas, text=codetext, justify=LEFT, font=('courier', '8', 'normal'))
        label = Label(canvas, text=self.text, justify=LEFT,
                      font=("tahoma", "8", "normal"))
        codelabel.grid(row=0, column=0)
        label.grid(row=1, column=0)


    def hide(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, codetext, text):
    popup = PopupsButtons(widget)

    def enter(event):
        time.sleep(0.5)
        popup.show(codetext, text)

    def leave(event):
        popup.hide()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)