import turtle

screen = turtle.Screen()
image = "/home/jibril/Documents/Python/DAY-25/US_States_Game/blank_states_img.gif"
screen.title("U.S States Game")
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
# screen.exitonclick()
