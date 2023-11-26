from turtle import Screen
from SnakeGame.snake import Snake
from SnakeGame.food import Food
from SnakeGame.scoreboard import Scoreboard
import time


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("@rublaman Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 10:
            food.refresh()
            scoreboard.increase_scoreboard()

    screen.exitonclick()
