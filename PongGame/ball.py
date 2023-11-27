from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.03

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def hit_wall(self):
        self.goto(0, 0)
        self.y_move *= -1
        self.x_move *= -1
