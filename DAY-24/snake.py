from turtle import Turtle, Screen

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
FORWAD_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        segment1 = Turtle("square")

        segment1.color("white")
        segment1.penup()

        segment1.goto(position)
        self.segments.append(segment1)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.head.forward(FORWAD_DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
