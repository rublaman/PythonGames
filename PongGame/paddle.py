from turtle import Turtle

UP = 90
DOWN = 270
STEP = 20


class Paddle(Turtle):

    def __init__(self, position: tuple):
        super().__init__()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


