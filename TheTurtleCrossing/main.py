import time
from turtle import Screen
from TheTurtleCrossing.player import Player
from TheTurtleCrossing.car_manager import CarManager
from TheTurtleCrossing.scoreboard import Scoreboard


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    turtle = Player()
    scoreboard = Scoreboard()
    cars = CarManager()

    screen.onkey(turtle.move_up, "Up")
    screen.onkey(turtle.move_left, "Left")
    screen.onkey(turtle.move_right, "Right")

    screen.listen()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        cars.move()

        if turtle.ycor() > 280:
            turtle.finish_line()
            scoreboard.increase_scoreboard()
            cars.increment_speed()

        for car in cars.list_of_cars:
            if car.distance(turtle) < 20:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()