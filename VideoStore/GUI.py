from tkinter import *

# create window
win = Tk()
win.title("Film Inventory Management System")
win.geometry('700x700')
win.configure(bg='black')


# widgets
title = Label(win, text='Film Inventory Tracker', bg='black', fg='white', font='Helvetica 25 bold')\
    .place(relx=.5, rely=.020, anchor=CENTER)
choice = Entry(win, text='Enter a choice...', fg='white', bg='black')\
    .place(relx=.5, rely=.8, anchor=CENTER)

# button = Button(win, text='Button 1').grid(row=1, column=0, sticky=W)

# packing widgets
# title.pack()
# button.pack()


# run the main loop
win.mainloop()


