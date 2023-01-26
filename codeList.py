import sandbox
from CodeButton import *
from CollapsablePane import CollapsiblePane as cp

# variables
variableIs = CodeButton('New Variable', '<var> = <value>')
globalVarIs = CodeButton('New global variable', 'global <var>\n<var> = <value>')
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
ifElse = CodeButton('If statement', 'if <condition>:\n\t<command>')
elifStatement = CodeButton('else if', 'elif <condition>:\n\t<command>')
elseStatement = CodeButton('else...', 'else:\n\t<command>')
#switchCase = CodeButton('switch case', '')

#Loops
whileLoop = CodeButton('while...', 'while <condition>:\n\t<command>')
forLoop = CodeButton("Do it (X) times", "for x in range (insert):\n\t(insert code)")
forLoopList = CodeButton('for each element...', 'for x in <list>:\n\t<command>')

#define function
defFun = CodeButton('define function', 'def <function_name>(<args>):\n\t<command>')

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
    varspane = cp(codeListFrame, 'close', 'open')
    varspane.grid(row=0, column=0)

    varisbtn = Button(varspane.frame, text=variableIs.name,
                           command=lambda: parseText(variableIs.codetext, sandbox.textarea))
    varisbtn.grid(
        row=1, column=0)

    globalvarbtn = Button(varspane.frame, text=globalVarIs.name,
                        command=lambda: parseText(globalVarIs.codetext, sandbox.textarea))
    globalvarbtn.grid(
        row=2, column=0)

    setvarbtn = Button(varspane.frame, text=setVar.name,
                          command=lambda: parseText(setVar.codetext, sandbox.textarea))
    setvarbtn.grid(
        row=3, column=0)

    incrembtn = Button(varspane.frame, text=incrementVar.name,
                          command=lambda: parseText(incrementVar.codetext, sandbox.textarea))
    incrembtn.grid(
        row=4, column=0)

    decrembtn = Button(varspane.frame, text=decrementVar.name,
                          command=lambda: parseText(decrementVar.codetext, sandbox.textarea))
    decrembtn.grid(
        row=5, column=0)

    listpane = cp(codeListFrame, 'close', 'open')
    listpane.grid(row=6, column=0)

    newlistbtn = Button(listpane.frame, text=newList.name,
                       command=lambda: parseText(newList.codetext, sandbox.textarea))
    newlistbtn.grid(
        row=7, column=0)

    findelembtn = Button(listpane.frame, text=findElem.name,
                        command=lambda: parseText(findElem.codetext, sandbox.textarea))
    findelembtn.grid(
        row=8, column=0)

    findindexbtn = Button(listpane.frame, text=findIndex.name,
                        command=lambda: parseText(findIndex.codetext, sandbox.textarea))
    findindexbtn.grid(
        row=9, column=0)

    appendbtn = Button(listpane.frame, text=addEndToList.name,
                        command=lambda: parseText(addEndToList.codetext, sandbox.textarea))
    appendbtn.grid(
        row=10, column=0)

    insertbtn = Button(listpane.frame, text=addLocToList.name,
                        command=lambda: parseText(addLocToList.codetext, sandbox.textarea))
    insertbtn.grid(
        row=11, column=0)

    removebtn = Button(listpane.frame, text=remfromList.name,
                        command=lambda: parseText(remfromList.codetext, sandbox.textarea))
    removebtn.grid(
        row=12, column=0)

    lenlistbtn = Button(listpane.frame, text=lenList.name,
                        command=lambda: parseText(lenList.codetext, sandbox.textarea))
    lenlistbtn.grid(
        row=13, column=0)

    reversebtn = Button(listpane.frame, text=reverseList.name,
                        command=lambda: parseText(reverseList.codetext, sandbox.textarea))
    reversebtn.grid(
        row=14, column=0)

    sortbtn = Button(listpane.frame, text=sortList.name,
                        command=lambda: parseText(sortList.codetext, sandbox.textarea))
    sortbtn.grid(
        row=15, column=0)

    condpane = cp(codeListFrame, 'close', 'open')
    condpane.grid(row=16, column=0)

    ifelsebtn = Button(condpane.frame, text=ifElse.name,
                     command=lambda: parseText(ifElse.codetext, sandbox.textarea))
    ifelsebtn.grid(
        row=17, column=0)

    elifbtn = Button(condpane.frame, text=elifStatement.name,
                       command=lambda: parseText(elifStatement.codetext, sandbox.textarea))
    elifbtn.grid(
        row=18, column=0)

    elsebtn = Button(condpane.frame, text=elseStatement.name,
                       command=lambda: parseText(elseStatement.codetext, sandbox.textarea))
    elsebtn.grid(
        row=19, column=0)

    looppane = cp(codeListFrame, 'close', 'open')
    looppane.grid(row=20, column=0)

    whilebtn = Button(looppane.frame, text=whileLoop.name,
                     command=lambda: parseText(whileLoop.codetext, sandbox.textarea))
    whilebtn.grid(
        row=21, column=0)

    forbtn = Button(looppane.frame, text=forLoop.name,
                      command=lambda: parseText(forLoop.codetext, sandbox.textarea))
    forbtn.grid(
        row=22, column=0)

    forlistbtn = Button(looppane.frame, text=forLoopList.name,
                      command=lambda: parseText(forLoopList.codetext, sandbox.textarea))
    forlistbtn.grid(
        row=23, column=0)

    logpane = cp(codeListFrame, 'close', 'open')
    logpane.grid(row=24, column=0)

    andbtn = Button(logpane.frame, text=andOp.name,
                        command=lambda: parseText(andOp.codetext, sandbox.textarea))
    andbtn.grid(
        row=25, column=0)

    orbtn = Button(logpane.frame, text=orOp.name,
                    command=lambda: parseText(orOp.codetext, sandbox.textarea))
    orbtn.grid(
        row=26, column=0)

    notbtn = Button(logpane.frame, text=notOp.name,
                   command=lambda: parseText(notOp.codetext, sandbox.textarea))
    notbtn.grid(
        row=27, column=0)

    comppane = cp(codeListFrame, 'close', 'open')
    comppane.grid(row=28, column=0)

    greaterbtn = Button(comppane.frame, text=isGreater.name,
                    command=lambda: parseText(isGreater.codetext, sandbox.textarea))
    greaterbtn.grid(
        row=29, column=0)

    greateroreqbtn = Button(comppane.frame, text=isGreaterOrEq.name,
                        command=lambda: parseText(isGreaterOrEq.codetext, sandbox.textarea))
    greateroreqbtn.grid(
        row=30, column=0)

    lessbtn = Button(comppane.frame, text=isLess.name,
                        command=lambda: parseText(isLess.codetext, sandbox.textarea))
    lessbtn.grid(
        row=31, column=0)

    lessoreqbtn = Button(comppane.frame, text=isLessorEq.name,
                     command=lambda: parseText(isLessorEq.codetext, sandbox.textarea))
    lessoreqbtn.grid(
        row=32, column=0)

    equalbtn = Button(comppane.frame, text=isEqual.name,
                     command=lambda: parseText(isEqual.codetext, sandbox.textarea))
    equalbtn.grid(
        row=33, column=0)

    noteqbtn = Button(comppane.frame, text=isNotEqual.name,
                     command=lambda: parseText(isNotEqual.codetext, sandbox.textarea))
    noteqbtn.grid(
        row=34, column=0)

    mempane = cp(codeListFrame, 'close', 'open')
    mempane.grid(row=35, column=0)

    isinbtn = Button(mempane.frame, text=isItIn.name,
                     command=lambda: parseText(isItIn.codetext, sandbox.textarea))
    isinbtn.grid(
        row=36, column=0)

    isnotinbtn = Button(mempane.frame, text=isItNotIn.name,
                     command=lambda: parseText(isItNotIn.codetext, sandbox.textarea))
    isnotinbtn.grid(
        row=37, column=0)


    return codeListFrame
