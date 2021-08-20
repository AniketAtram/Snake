from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score : {self.score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)