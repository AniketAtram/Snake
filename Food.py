from turtle import Turtle
import random
COLORS = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(COLORS))
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        pos_x = random.randint(-260, 260)
        pos_y = random.randint(-260, 260)
        self.goto(pos_x, pos_y)