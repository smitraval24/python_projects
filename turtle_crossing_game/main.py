import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manage = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manage.generate_cars()
    car_manage.move()
    if player.ycor() == 300:
        scoreboard.increase_score()
        car_manage.increase_speed()
        player.reset()
    else:
        scoreboard.show_score()

    for car in car_manage.all_cars:
        if car.distance(player) <= 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()