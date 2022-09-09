from tkinter import *


root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=55, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# e.insert(0,'Enter your Name: ')
def buttonClick(num):
    curr = e.get()
    e.delete(0,END)
    e.insert(0, str(curr) + str(num))

def add():
    firstNum = e.get()
    global fNum
    global math
    math = 'addition'
    fNum = int(firstNum)
    e.delete(0,END)

def subtract():
    firstNum = e.get()
    global fNum
    global math
    math = 'subtraction'
    fNum = int(firstNum)
    e.delete(0,END)

def multiply():
    firstNum = e.get()
    global fNum
    global math
    math = 'multiplication'
    fNum = int(firstNum)
    e.delete(0,END)

def divide():
    firstNum = e.get()
    global fNum
    global math
    math = 'division'
    fNum = int(firstNum)
    e.delete(0,END)

def equal():
    secNum = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0, int(fNum) + int(secNum))
    elif math == 'subtraction':
        e.insert(0, int(fNum) - int(secNum))
    elif math == 'multiplication':
        e.insert(0, int(fNum) * int(secNum))
    elif math == 'division':
        e.insert(0, int(fNum) / int(secNum))

def clear():
    e.delete(0,END)

# define buttons
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: buttonClick(0))
plusButton = Button(root, text='+', padx=38, pady=20, command=add)
minusButton = Button(root, text='-', padx=39, pady=20, command=subtract)
multipyButton = Button(root, text='*', padx=39, pady=20, command=multiply)
divideButton = Button(root, text='/', padx=39, pady=20, command=divide)
equalButton = Button(root, text='=', padx=91, pady=20, command=equal)
clearButton = Button(root, text='Clear', padx=79, pady=20, command=clear)

# putting the buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
clearButton.grid(row=4, column=1, columnspan=2)
equalButton.grid(row=5, column=1, columnspan=2)

plusButton.grid(row=1, column=3)
minusButton.grid(row=2, column=3)
multipyButton.grid(row=3, column=3)
divideButton.grid(row=4, column=3)


root.mainloop()
