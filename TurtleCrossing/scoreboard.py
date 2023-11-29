from turtle import Screen
import time

FONT = ("Courier", 24, "normal")


class Scoreboard:

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    is_game_on = True
    while is_game_on:
        time.sleep(0.1)
        screen.update()

