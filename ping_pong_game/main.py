import turtle
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
scoreboard = ScoreBoard()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
turtle.speed("slow")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.moveup, "Up")
screen.onkeypress(r_paddle.movedown, "Down")
screen.onkeypress(l_paddle.moveup, "w")
screen.onkeypress(l_paddle.movedown, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player1_score()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player2_score()

    scoreboard.update_scoreboard()

screen.exitonclick()