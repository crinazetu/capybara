from CodeButton import *
import sandbox
import PopupsButtons
import codeList
from CollapsablePane import CollapsiblePane as cp

variableIs = CodeButton('New Variable', '<var> = <value>')
globalVarIs = CodeButton('New global variable', 'global <var>\n<var> = <value>')
setVar = CodeButton('Set Variable to...', '<var> = <newValue>')
incrementVar = CodeButton('Increment Value', '<var> += 1')
decrementVar = CodeButton('Decrement Value', '<var> -= 1')

# lists
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
# switchCase = CodeButton('switch case', '')

# Loops
whileLoop = CodeButton('while...', 'while <condition>:\n\t<command>')
forLoop = CodeButton("Do it (X) times", "for x in range (insert):\n\t(insert code)")
forLoopList = CodeButton('for each element...', 'for x in <list>:\n\t<command>')

# define function
defFun = CodeButton('define function', 'def <function_name>(<args>):\n\t<command>')

# operators
# logical
andOp = CodeButton('and', '<cond1> and <cond2>')
orOp = CodeButton('or', '<cond1> or <cond2>')
notOp = CodeButton('not', 'not(<cond>)')
# comparison
isGreater = CodeButton('greater than...', '<value1> > <value2>')
isGreaterOrEq = CodeButton('greater or equal than...', '<value1> >= <value2>')
isLess = CodeButton('less than...', '<value1> < <value2>')
isLessorEq = CodeButton('less or equal than...', '<value1> <= <value2>')
isEqual = CodeButton('equal to...', '<value1> == <value2>')
isNotEqual = CodeButton('NOT equal to...', '<value1> != <value2>')
# membership
isItIn = CodeButton('Is element in list', '<element> in <list>')
isItNotIn = CodeButton('Is element NOT in list', '<element> not in <list>')

# misc
helloWorld = CodeButton("Say Hello world", "print(\"Hello world\")")


def createList(frame):
    list = []


    varisbtn = Button(frame,text=variableIs.name,
                      command=lambda: parseText(variableIs.codetext, sandbox.textarea))
    list.append(varisbtn)
    PopupsButtons.CreateToolTip(varisbtn, variableIs.codetext + "\ncreates a variable")

    globalvarbtn = Button(frame, text=globalVarIs.name,
                          command=lambda: parseText(globalVarIs.codetext, sandbox.textarea))
    list.append(globalvarbtn)

    setvarbtn = Button(frame, text=setVar.name,
                       command=lambda: parseText(setVar.codetext, sandbox.textarea))
    list.append((setvarbtn))


    incrembtn = Button(frame, text=incrementVar.name,
                       command=lambda: parseText(incrementVar.codetext, sandbox.textarea))
    list.append(incrembtn)

    decrembtn = Button(frame, text=decrementVar.name,
                       command=lambda: parseText(decrementVar.codetext, sandbox.textarea))
    list.append(decrembtn)

    newlistbtn = Button(frame, text=newList.name,
                        command=lambda: parseText(newList.codetext, sandbox.textarea))
    list.append(newlistbtn)

    findelembtn = Button(frame, text=findElem.name,
                         command=lambda: parseText(findElem.codetext, sandbox.textarea))
    list.append(findelembtn)

    findindexbtn = Button(frame, text=findIndex.name,
                          command=lambda: parseText(findIndex.codetext, sandbox.textarea))
    list.append(findindexbtn)

    appendbtn = Button(frame, text=addEndToList.name,
                       command=lambda: parseText(addEndToList.codetext, sandbox.textarea))
    list.append(appendbtn)
    insertbtn = Button(frame, text=addLocToList.name,
                       command=lambda: parseText(addLocToList.codetext, sandbox.textarea))
    list.append(insertbtn)
    removebtn = Button(frame, text=remfromList.name,
                       command=lambda: parseText(remfromList.codetext, sandbox.textarea))
    list.append(removebtn)
    lenlistbtn = Button(frame, text=lenList.name,
                        command=lambda: parseText(lenList.codetext, sandbox.textarea))
    list.append(lenlistbtn)
    reversebtn = Button(frame, text=reverseList.name,
                        command=lambda: parseText(reverseList.codetext, sandbox.textarea))
    list.append(reversebtn)
    sortbtn = Button(frame, text=sortList.name,
                     command=lambda: parseText(sortList.codetext, sandbox.textarea))
    list.append(sortbtn)
    ifelsebtn = Button(frame, text=ifElse.name,
                       command=lambda: parseText(ifElse.codetext, sandbox.textarea))
    list.append(ifelsebtn)
    elifbtn = Button(frame, text=elifStatement.name,
                     command=lambda: parseText(elifStatement.codetext, sandbox.textarea))
    list.append(elifbtn)
    elsebtn = Button(frame, text=elseStatement.name,
                     command=lambda: parseText(elseStatement.codetext, sandbox.textarea))
    list.append(elsebtn)
    whilebtn = Button(frame, text=whileLoop.name,
                      command=lambda: parseText(whileLoop.codetext, sandbox.textarea))
    list.append(whilebtn)
    forbtn = Button(frame, text=forLoop.name,
                    command=lambda: parseText(forLoop.codetext, sandbox.textarea))
    list.append(forbtn)
    forlistbtn = Button(frame, text=forLoopList.name,
                        command=lambda: parseText(forLoopList.codetext, sandbox.textarea))
    list.append(forlistbtn)
    andbtn = Button(frame, text=andOp.name,
                    command=lambda: parseText(andOp.codetext, sandbox.textarea))
    list.append(andbtn)
    orbtn = Button(frame, text=orOp.name,
                   command=lambda: parseText(orOp.codetext, sandbox.textarea))
    list.append(orbtn)
    notbtn = Button(frame, text=notOp.name,
                    command=lambda: parseText(notOp.codetext, sandbox.textarea))
    list.append(notbtn)
    greaterbtn = Button(frame, text=isGreater.name,
                        command=lambda: parseText(isGreater.codetext, sandbox.textarea))
    list.append(greaterbtn)
    greateroreqbtn = Button(frame, text=isGreaterOrEq.name,
                            command=lambda: parseText(isGreaterOrEq.codetext, sandbox.textarea))
    list.append(greateroreqbtn)
    lessbtn = Button(frame, text=isLess.name,
                     command=lambda: parseText(isLess.codetext, sandbox.textarea))
    list.append(lessbtn)
    lessoreqbtn = Button(frame, text=isLessorEq.name,
                         command=lambda: parseText(isLessorEq.codetext, sandbox.textarea))
    list.append(lessoreqbtn)
    equalbtn = Button(frame, text=isEqual.name,
                      command=lambda: parseText(isEqual.codetext, sandbox.textarea))
    list.append(equalbtn)
    noteqbtn = Button(frame, text=isNotEqual.name,
                      command=lambda: parseText(isNotEqual.codetext, sandbox.textarea))
    list.append(noteqbtn)
    isinbtn = Button(frame, text=isItIn.name,
                     command=lambda: parseText(isItIn.codetext, sandbox.textarea))
    list.append(isinbtn)
    isnotinbtn = Button(frame, text=isItNotIn.name,
                        command=lambda: parseText(isItNotIn.codetext, sandbox.textarea))
    list.append(isnotinbtn)
    return list

def parseText(code, textarea):
    ins = code
    textarea.insert(INSERT, ins)
