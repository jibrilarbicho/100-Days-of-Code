import turtle

screen = turtle.Screen()
image = "/home/jibril/Documents/Python/DAY-25/US_States_Game/blank_states_img.gif"
screen.title("U.S States Game")
screen.addshape(image)

turtle.shape(image)
import pandas

guessed_states = []


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=(f"{len(guessed_states)}/50 Staes Correct"),
        prompt="What is another state Name?",
    ).title()
    print(answer_state)

    data = pandas.read_csv(
        "/home/jibril/Documents/Python/DAY-25/US_States_Game/50_states.csv"
    )
    StateList = data.state.tolist()
    if answer_state in StateList:
        t = turtle.Turtle()
        guessed_states.append(answer_state)
        t.hideturtle()
        t.penup()
        stateData = data[data.state == answer_state]
        t.goto(int(stateData.x), int(stateData.y))
        # t.write(answer_state)
        t.write(stateData.state.item())


turtle.mainloop()
# screen.exitonclick()
