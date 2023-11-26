from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_segment_list: list[Turtle] = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            snake_block = Turtle("square")
            snake_block.color("white")
            snake_block.penup()
            snake_block.goto(i * -20, 0)
            self.snake_segment_list.append(snake_block)

    def move(self):
        for segment_position in range(len(self.snake_segment_list) - 1, 0, -1):
            new_x = self.snake_segment_list[segment_position - 1].xcor()
            new_y = self.snake_segment_list[segment_position - 1].ycor()
            self.snake_segment_list[segment_position].goto(new_x, new_y)
        self.snake_segment_list[0].forward(20)
