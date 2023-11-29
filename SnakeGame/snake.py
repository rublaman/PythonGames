from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segment_list: list[Turtle] = []
        self.create_snake()
        self.head = self.snake_segment_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_block = Turtle("square")
        snake_block.color("white")
        snake_block.penup()
        snake_block.goto(position)
        self.snake_segment_list.append(snake_block)

    def reset(self):
        for segment in self.snake_segment_list:
            segment.goto(1000, 1000)
        self.snake_segment_list.clear()
        self.create_snake()
        self.head = self.snake_segment_list[0]

    def extend_segment(self):
        self.add_segment(self.snake_segment_list[-1].position())

    def move(self):
        for segment_position in range(len(self.snake_segment_list) - 1, 0, -1):
            new_x = self.snake_segment_list[segment_position - 1].xcor()
            new_y = self.snake_segment_list[segment_position - 1].ycor()
            self.snake_segment_list[segment_position].goto(new_x, new_y)
        self.head.forward(MOVE_STEP_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
