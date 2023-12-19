import tkinter

window = tkinter.Tk()


window.title("MY First GUI Program")

window.minsize(width=500, height=300)


mylabel = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

mylabel.pack()
window.mainloop()
