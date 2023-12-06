from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
# screen.listen()


# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)


# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)


# def clear():
#     tim.clear()
#     tim.home()


# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# timy = Turtle()
# tomy = Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make Your Bet", prompt="Which Turtle will win the race ? Enter a Color"
)
y_positions = [-70, -40, -10, 20, 50, 80]
print(user_bet)
for turtle_index in range(0, 6):
    tim = Turtle()
    tim.penup()

    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.shape("turtle")


screen.exitonclick()
