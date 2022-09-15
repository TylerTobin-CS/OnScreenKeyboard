#Tyler Tobin
#On screen keyboard
#can be put within a class to be used within other projects

from tkinter import *
import tkinter

onScreen = tkinter.Tk()
onScreen.title("OnScreenKey")
onScreen.geometry("1250x200")

def buttonSelect(value):
    if value == "<-":
        entry2 = entry.get()
        pos = entry2.find("")
        posAdd = entry2[pos:]
        entry.delete(posAdd, tkinter.END)
    else:
        entry.insert(tkinter.END, value)

buttonsToPress = [
"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "7", "8", "9","a", "s", "d", "f", "g", "h", "j", "k", "l", "[", "]", "4", "5", "6",
"z", "x", "c", "v", "b", "n", "m", ",", ".", "?", "1", "2", "3"]

varRow = 2
varColumn = 0

entry = Entry(onScreen, width = 130)
entry.grid(row = 1, columnspan = 20)

for button in buttonsToPress:
    command = lambda x = button: buttonSelect(x)
    if button != "space":
        tkinter.Button(onScreen, text = button, width = 5, command = command).grid(row = varRow, column = varColumn)

    varColumn += 1
    if varColumn > 14:
        varColumn = 0
        varRow += 1
    if varColumn > 14:
        varColumn = 0
        varRow += 1

onScreen.mainloop()
