from turtle import Turtle, Screen


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("@rublaman Snake Game")

    snake_segment_list = []
    create_snake(snake_segment_list)

    screen.exitonclick()


def create_snake(snake_segment_list: list[Turtle]):
    new_snake_segment_list = snake_segment_list
    if len(snake_segment_list) == 0:
        for i in range(0, 3):
            snake_block = Turtle("square")
            snake_block.color("white")
            snake_block.penup()
            snake_block.goto(i * -20, 0)
            new_snake_segment_list.append(snake_block)

