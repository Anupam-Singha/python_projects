from tkinter import *

root = Tk()

def myClick():
    myLabel1 = Label(root, text="The button is working", padx=50, pady=50)
    myLabel1.pack()

myButton = Button(root, text="Click me!", command=myClick)
myButton.pack()

root.mainloop()