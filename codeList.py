import sandbox
from CodeButton import *

#btnDict = {}

helloWorld = CodeButton("Say Hello world", "print(\"Hello world\")")
forLoop = CodeButton("Do it (X) times", "for x in range (insert): \n \t (insert code)")

#btnDict["helloworld"] = helloWorld
#btnDict["forLoop"] = forLoop

def parseText(code, textarea):
    ins = code
    textarea.insert(INSERT, ins)
def createGUI(parentframe):
    global codeListFrame
    codeListFrame = LabelFrame(parentframe, text="Code List", font=('courier', 12, 'bold'))
    #for key, button in btnDict.items():
    #    key = Button(codeListFrame, text=button.name, command=lambda: parseText(button.codetext, sandbox.textarea))
    #    key.pack()

    helloworldbtn = Button(codeListFrame, text=helloWorld.name, command=lambda: parseText(helloWorld.codetext, sandbox.textarea))
    helloworldbtn.pack()
    forloopbtn = Button(codeListFrame, text=forLoop.name, command=lambda: parseText(forLoop.codetext, sandbox.textarea))
    forloopbtn.pack()

    return codeListFrame


