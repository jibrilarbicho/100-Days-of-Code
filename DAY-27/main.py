from os import initgroups
from tkinter import *

import comm

window = Tk()


window.title("MY First GUI Program")

window.minsize(width=500, height=300)


mylabel = Label(text="I am a label", font=("Arial", 24, "bold"))

input = Entry(width=10)


def button_clicked():
    print("i am clicked")
    print(input.get())
    mylabel.config(text="Button clicked")


button = Button(text="Click ME", command=button_clicked)
mylabel.place(x=100, y=100)
button.pack()
input.pack()
window.mainloop()
