from curses import window
from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile To Kilometer Converter")
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)
miles_input = Entry()

miles_input.grid(column=1, row=0)
miles_label = Label(text="MILES")
miles_label.grid(column=2, row=0)
isequalLael = Label(text="is equal to")
isequalLael.grid(column=0, row=1)
kilometer_result_label = Label(text="0", font=("Arial", 10, "bold"))
kilometer_result_label.grid(column=1, row=1)
kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
