from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", move=None, align='Left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=None, align='Left', font=FONT)
