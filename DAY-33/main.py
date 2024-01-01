# from traceback import print_tb
# import requests

# res = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if res.status_code == 404:
# #     raise Exception("The Resource Does not found")
# # elif res.status_code == 401:
# #     raise Exception("You are not Authorized to access this data")
# res.raise_for_status()

# data = res.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    result = response.json()
    quote = result["quote"]
    # Write your code here.
    canvas.itemconfig(quote_text, quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="/home/jibril/Documents/Python/DAY-33/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="/home/jibril/Documents/Python/DAY-33/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
