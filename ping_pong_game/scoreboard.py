from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.score1}", align="center", font=("Courier", 40, "normal"))
        self.goto(100, 240)
        self.write(f"{self.score2}", align="center", font=("Courier", 40, "normal"))

    def player1_score(self):
        self.score1 += 1
        self.update_scoreboard()

    def player2_score(self):
        self.score2 += 1
        self.update_scoreboard()
