from turtle import Screen
from PongGame.paddle import Paddle
import time


def start():

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))

    screen.listen()

    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "Up")
    screen.onkey(left_paddle.down, "Down")

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)

    screen.exitonclick()
