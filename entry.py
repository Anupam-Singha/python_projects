from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="violet")
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    mylabel1 = Label(root, text=e.get())
    mylabel1.pack()

myButton = Button(root, text="Click me", command=myClick)
myButton.pack()

root.mainloop()