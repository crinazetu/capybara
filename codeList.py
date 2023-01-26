import sandbox
from CodeButton import *
from CollapsablePane import CollapsiblePane as cp

# variables
variableIs = CodeButton('New Variable', '<var> = <value>')
globalVarIs = CodeButton('New global variable', 'global <var> \n <var> = <value>')
setVar = CodeButton('Set Variable to...', '<var> = <newValue>')
incrementVar = CodeButton('Increment Value', '<var> += 1')
decrementVar = CodeButton('Decrement Value', '<var> -= 1')

#lists
newList = CodeButton('New List', '<list> = [<elem1>, <elem2>, <elem3>]')
findElem = CodeButton('Find Element', '')
findIndex = CodeButton('find index of element', '<list>.index(<element>)')
addEndToList = CodeButton('Add element to end', '<list>.append(<element>)')
addLocToList = CodeButton('Add element to location', '<list>.insert(<index>, <element>)')
remfromList = CodeButton('Remove element', '<list>.remove(<element>)')
lenList = CodeButton('get length of list', 'len(<list>)')
reverseList = CodeButton('reverse order of list', '<list>.reverse()')
sortList = CodeButton('sort list', '<list>.sort()')

# Conditionals
ifElse = CodeButton('If-else statement', 'if <condition>: \n \t <command>')
elifStatement = CodeButton('else if', 'elif <condition>: \n \t <command>')
elseStatement = CodeButton('else...', 'else: \n \t <command>')
#switchCase = CodeButton('switch case', '')

#Loops
whileLoop = CodeButton('while...', 'while <condition>: \n \t <command>')
forLoop = CodeButton("Do it (X) times", "for x in range (insert): \n \t (insert code)")
forLoopList = CodeButton('for each element...', 'for x in <list>: \n \t <command>')

#define function
defFun = CodeButton('define function', 'def <function_name>(<args>): \n \t <command>')

#operators
#logical
andOp = CodeButton('and', '<cond1> and <cond2>')
orOp = CodeButton('or', '<cond1> or <cond2>')
notOp = CodeButton('not', 'not(<cond>)')
#comparison
isGreater = CodeButton('greater than...', '<value1> > <value2>')
isGreaterOrEq = CodeButton('greater or equal than...', '<value1> >= <value2>')
isLess = CodeButton('less than...', '<value1> < <value2>')
isLessorEq = CodeButton('less or equal than...', '<value1> <= <value2>')
isEqual = CodeButton('equal to...', '<value1> == <value2>')
isNotEqual = CodeButton('NOT equal to...', '<value1> != <value2>')
containsOp = CodeButton('does it contain...', '')
#membership
isItIn = CodeButton('Is element in list', '<element> in <list>')
isItNotIn = CodeButton('Is element NOT in list', '<element> not in <list>')

#misc
helloWorld = CodeButton("Say Hello world", "print(\"Hello world\")")

def parseText(code, textarea):
    ins = code
    textarea.insert(INSERT, ins)


def createGUI(parentframe):
    global codeListFrame
    codeListFrame = LabelFrame(parentframe, text="Code List", font=('courier', 12, 'bold'))

    mainpane = cp(codeListFrame, 'close', 'open')
    mainpane.grid(row=0, column=0)

    helloworldbtn = Button(mainpane.frame, text=helloWorld.name,
                           command=lambda: parseText(helloWorld.codetext, sandbox.textarea))
    helloworldbtn.grid(
        row=1, column=0)

    forloopbtn = Button(mainpane.frame, text=forLoop.name,
                        command=lambda: parseText(forLoop.codetext, sandbox.textarea))
    forloopbtn.grid(
        row=2, column=0)

    return codeListFrame
