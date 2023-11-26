from turtle import Screen
from SnakeGame.snake import Snake
import time


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("@rublaman Snake Game")
    screen.tracer(0)

    snake = Snake()

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

    screen.exitonclick()

