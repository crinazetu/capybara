from CodeButton import *
import sandbox
import PopupsButtons
from tkinter import ttk
import codeList
from CollapsablePane import CollapsiblePane as cp

variableIs = CodeButton('New Variable', 'insert_variable_name = insert-value')
globalVarIs = CodeButton('New global variable', 'global insert_variable_name\ninsert_variable_name = insert-value')
#setVar = CodeButton('Set Variable to...', '<var> = <newValue>')
incrementVar = CodeButton('Increment Value', 'variable_name += 1')
decrementVar = CodeButton('Decrement Value', 'variable_name -= 1')

# lists
newList = CodeButton('New List', 'insert_list_name = [element_1, element_2, element_3]')
getElem = CodeButton('Find Element', 'insert_list_name[index_number]')
findIndex = CodeButton('Find index of element', 'insert_list_name.index(element_name)')
addEndToList = CodeButton('Add element to end', 'insert_list_name.append(element_name)')
addLocToList = CodeButton('Add element to location', 'insert_list_name.insert(insert_index_number, element_name)')
remfromList = CodeButton('Remove element', 'insert_list_name.remove(element_name)')
lenList = CodeButton('Get length of list', 'len(insert_list_name)')
reverseList = CodeButton('Reverse order of list', 'insert_list_name.reverse()')
sortList = CodeButton('Sort list', 'insert_list_name.sort()')

# Conditionals
ifElse = CodeButton('If statement', 'if (state_the_condition):\n\t#insert commands...')
elifStatement = CodeButton('Else if', 'elif (state_the_condition):\n\t#insert commands...')
elseStatement = CodeButton('Else...', 'else:\n\t#insert commands...')

# Loops
whileLoop = CodeButton('While...', 'while (state_the_condition):\n\t#insert commands...')
forLoop = CodeButton("For a number of times...", "for x in range (number_of_times):\n\t#insert commands...")
forLoopList = CodeButton('For each element...', 'for x in insert_list_name:\n\t#insert commands...')

# define function
defFun = CodeButton('Define a function', 'def insert_function_name(state_the_parameters):\n\t#insert commands...')

# operators
# logical
andOp = CodeButton('and', '(condition_1) and (condition_2)')
orOp = CodeButton('or', '(condition_1) or (condition_2)')
notOp = CodeButton('not', 'not(condition)')
# comparison
isGreater = CodeButton('greater than...', 'insert_value_1 > insert_value_2')
isGreaterOrEq = CodeButton('greater or equal than...', 'insert_value_1 >= insert_value_2')
isLess = CodeButton('less than...', 'insert_value_1 < insert_value_2')
isLessorEq = CodeButton('less or equal than...', 'insert_value_1 <= insert_value_2')
isEqual = CodeButton('equal to...', 'insert_value_1 == insert_value_2')
isNotEqual = CodeButton('NOT equal to...', 'insert_value_1 != insert_value_2')
# membership
isItIn = CodeButton('Is element in list', 'specify_element in specify_list_name')
isItNotIn = CodeButton('Is element NOT in list', 'specify_element not in specify_list_name')

# misc
printmsg = CodeButton("Print a message", "print(\"Insert message here\")")


def createList(frame):
    list = []

    printmsgbtn = ttk.Button(frame, text=printmsg.name, command=lambda: parseText(printmsg.codetext, sandbox.textarea))
    list.append(printmsgbtn)
    PopupsButtons.CreateToolTip(printmsgbtn, printmsg.codetext, 'Lets you print a written message in the output')


    varisbtn = ttk.Button(frame,text=variableIs.name,
                      command=lambda: parseText(variableIs.codetext, sandbox.textarea))
    list.append(varisbtn)
    PopupsButtons.CreateToolTip(varisbtn, variableIs.codetext, "Creates a variable")

    globalvarbtn = ttk.Button(frame, text=globalVarIs.name,
                          command=lambda: parseText(globalVarIs.codetext, sandbox.textarea))
    list.append(globalvarbtn)
    PopupsButtons.CreateToolTip(globalvarbtn, globalVarIs.codetext, "Creates a global variable.\nIt needs to be declared first, and then assigned a value")

    #setvarbtn = ttk.Button(frame, text=setVar.name,
                     #  command=lambda: parseText(setVar.codetext, sandbox.textarea))
    #list.append((setvarbtn))
    #PopupsButtons.CreateToolTip(setvarbtn, setVar.codetext, "Assigns a new value to an existing variable")


    incrembtn = ttk.Button(frame, text=incrementVar.name,
                       command=lambda: parseText(incrementVar.codetext, sandbox.textarea))
    list.append(incrembtn)
    PopupsButtons.CreateToolTip(incrembtn, incrementVar.codetext, "Adds 1 to the value of a variable, if it's a number")

    decrembtn = ttk.Button(frame, text=decrementVar.name,
                       command=lambda: parseText(decrementVar.codetext, sandbox.textarea))
    list.append(decrembtn)
    PopupsButtons.CreateToolTip(decrembtn, decrementVar.codetext, "Takes away 1 from a variable, if it's a number")

    newlistbtn = ttk.Button(frame, text=newList.name,
                        command=lambda: parseText(newList.codetext, sandbox.textarea))
    list.append(newlistbtn)
    PopupsButtons.CreateToolTip(newlistbtn, newList.codetext, "Creates a new list to assign elements to")

    findelembtn = ttk.Button(frame, text=getElem.name,
                         command=lambda: parseText(getElem.codetext, sandbox.textarea))
    list.append(findelembtn)
    PopupsButtons.CreateToolTip(findelembtn, getElem.codetext, "Returns an element of a list based off its index")

    findindexbtn = ttk.Button(frame, text=findIndex.name,
                          command=lambda: parseText(findIndex.codetext, sandbox.textarea))
    list.append(findindexbtn)
    PopupsButtons.CreateToolTip(findindexbtn, findIndex.codetext, "Returns the index of a specific element in a list")

    appendbtn = ttk.Button(frame, text=addEndToList.name,
                       command=lambda: parseText(addEndToList.codetext, sandbox.textarea))
    list.append(appendbtn)
    PopupsButtons.CreateToolTip(appendbtn, addEndToList.codetext, "Adds a new element to the end of the list")

    insertbtn = ttk.Button(frame, text=addLocToList.name,
                       command=lambda: parseText(addLocToList.codetext, sandbox.textarea))
    list.append(insertbtn)
    PopupsButtons.CreateToolTip(insertbtn, addLocToList.codetext, "Adds a new element at a specified location in the list")

    removebtn = ttk.Button(frame, text=remfromList.name,
                       command=lambda: parseText(remfromList.codetext, sandbox.textarea))
    list.append(removebtn)
    PopupsButtons.CreateToolTip(removebtn, remfromList.codetext, "Removes an element from a list at a specified location")

    lenlistbtn = ttk.Button(frame, text=lenList.name,
                        command=lambda: parseText(lenList.codetext, sandbox.textarea))
    list.append(lenlistbtn)
    PopupsButtons.CreateToolTip(lenlistbtn, lenList.codetext, "returns the number of elements in a list")

    reversebtn = ttk.Button(frame, text=reverseList.name,
                        command=lambda: parseText(reverseList.codetext, sandbox.textarea))
    list.append(reversebtn)
    PopupsButtons.CreateToolTip(reversebtn, reverseList.codetext, "reverses the order of elements in a list")

    sortbtn = ttk.Button(frame, text=sortList.name,
                     command=lambda: parseText(sortList.codetext, sandbox.textarea))
    list.append(sortbtn)
    PopupsButtons.CreateToolTip(sortbtn, sortList.codetext, "sorts the elements on the list in alphabetical or increasing order")

    ifelsebtn = ttk.Button(frame, text=ifElse.name,
                       command=lambda: parseText(ifElse.codetext, sandbox.textarea))
    list.append(ifelsebtn)
    PopupsButtons.CreateToolTip(ifelsebtn, ifElse.codetext, "Adds an if-else code block")

    elifbtn = ttk.Button(frame, text=elifStatement.name,
                     command=lambda: parseText(elifStatement.codetext, sandbox.textarea))
    list.append(elifbtn)
    PopupsButtons.CreateToolTip(elifbtn, elifStatement.codetext, "Elif is shorthand for else if. This is for adding more conditions in your if-else block")

    elsebtn = ttk.Button(frame, text=elseStatement.name,
                     command=lambda: parseText(elseStatement.codetext, sandbox.textarea))
    list.append(elsebtn)
    PopupsButtons.CreateToolTip(elsebtn, elseStatement.codetext, "Else is used in the if-else block is none of the conditions are met")

    whilebtn = ttk.Button(frame, text=whileLoop.name,
                      command=lambda: parseText(whileLoop.codetext, sandbox.textarea))
    list.append(whilebtn)
    PopupsButtons.CreateToolTip(whilebtn, whileLoop.codetext, "Adds a while loop. The code will always run as long as the condition is met")

    forbtn = ttk.Button(frame, text=forLoop.name,
                    command=lambda: parseText(forLoop.codetext, sandbox.textarea))
    list.append(forbtn)
    PopupsButtons.CreateToolTip(forbtn, forLoop.codetext, "Adds a for loop. The code will be run a specified number of times")

    forlistbtn = ttk.Button(frame, text=forLoopList.name,
                        command=lambda: parseText(forLoopList.codetext, sandbox.textarea))
    list.append(forlistbtn)
    PopupsButtons.CreateToolTip(forlistbtn, forLoopList.codetext, "Adds a for loop. The code will run for each element in a list")

    andbtn = ttk.Button(frame, text=andOp.name,
                    command=lambda: parseText(andOp.codetext, sandbox.textarea))
    list.append(andbtn)
    PopupsButtons.CreateToolTip(andbtn, andOp.codetext, "AND operator for two conditions. Code will run when BOTH conditions are met")

    orbtn = ttk.Button(frame, text=orOp.name,
                   command=lambda: parseText(orOp.codetext, sandbox.textarea))
    list.append(orbtn)
    PopupsButtons.CreateToolTip(orbtn, orOp.codetext, "OR operator for two conditions. Code will run when either or both conditons are met")

    notbtn = ttk.Button(frame, text=notOp.name,
                    command=lambda: parseText(notOp.codetext, sandbox.textarea))
    list.append(notbtn)
    PopupsButtons.CreateToolTip(notbtn, notOp.codetext, "NOT operator for a conditon. Code will run when the condition is NOT "+
                                               "met")

    greaterbtn = ttk.Button(frame, text=isGreater.name,
                        command=lambda: parseText(isGreater.codetext, sandbox.textarea))
    list.append(greaterbtn)
    PopupsButtons.CreateToolTip(greaterbtn, isGreater.codetext, "Checks if a value is larger than the other")

    greateroreqbtn = ttk.Button(frame, text=isGreaterOrEq.name,
                            command=lambda: parseText(isGreaterOrEq.codetext, sandbox.textarea))
    list.append(greateroreqbtn)
    PopupsButtons.CreateToolTip(greateroreqbtn, isGreaterOrEq.codetext, "Checks if a value is greater ot equal than "+
                                                                        "the other")

    lessbtn = ttk.Button(frame, text=isLess.name,
                     command=lambda: parseText(isLess.codetext, sandbox.textarea))
    list.append(lessbtn)
    PopupsButtons.CreateToolTip(lessbtn, isLess.codetext, "Checks if a value is smaller than the other")

    lessoreqbtn = ttk.Button(frame, text=isLessorEq.name,
                         command=lambda: parseText(isLessorEq.codetext, sandbox.textarea))
    list.append(lessoreqbtn)
    PopupsButtons.CreateToolTip(lessoreqbtn, isLessorEq.codetext, "Checks if a value is smaller or equal than another")

    equalbtn = ttk.Button(frame, text=isEqual.name,
                      command=lambda: parseText(isEqual.codetext, sandbox.textarea))
    list.append(equalbtn)
    PopupsButtons.CreateToolTip(equalbtn, isEqual.codetext, "Checks if a value is equal to another")

    noteqbtn = ttk.Button(frame, text=isNotEqual.name,
                      command=lambda: parseText(isNotEqual.codetext, sandbox.textarea))
    list.append(noteqbtn)
    PopupsButtons.CreateToolTip(noteqbtn, isNotEqual.codetext, "Checks if a value is NOT equal to another")

    isinbtn = ttk.Button(frame, text=isItIn.name,
                     command=lambda: parseText(isItIn.codetext, sandbox.textarea))
    list.append(isinbtn)
    PopupsButtons.CreateToolTip(isinbtn, isItIn.codetext, "Checks if an element is present in a list")

    isnotinbtn = ttk.Button(frame, text=isItNotIn.name,
                        command=lambda: parseText(isItNotIn.codetext, sandbox.textarea))
    list.append(isnotinbtn)
    PopupsButtons.CreateToolTip(isnotinbtn, isItNotIn.codetext, "Checks if an element is NOT in a list")
    return list

def parseText(code, textarea):
    ins = code
    textarea.insert(INSERT, ins)
