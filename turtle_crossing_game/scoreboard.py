FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)

    def show_score(self):
        self.clear()
        self.write("Level: " + str(self.level), font=(FONT))

    def increase_score(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)