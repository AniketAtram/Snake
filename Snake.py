from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.createTurtle()
        self.head = self.segments[0]
        self.head.color("green")

    def createTurtle(self):
        for pos in STARTING_POSITION:
            self.add_segments(pos)

    def extend_snake(self):
        self.add_segments(self.segments[-1].position())
        print(self.segments[-1].position())

    def add_segments(self, pos):
        my_turtle = Turtle("square")
        my_turtle.color("darkgreen")
        my_turtle.pu()
        my_turtle.goto(pos)
        self.segments.append(my_turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
