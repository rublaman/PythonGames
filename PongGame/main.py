from turtle import Screen
from PongGame.paddle import Paddle
from PongGame.ball import Ball
import time

WIDTH = 800
HEIGHT = 600



def start():

    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball()

    screen.listen()

    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "Up")
    screen.onkey(left_paddle.down, "Down")

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)

        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

    screen.exitonclick()
