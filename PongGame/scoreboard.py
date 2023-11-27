from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"Score: {self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"Score: {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_left_scoreboard(self):
        self.clear()
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_scoreboard(self):
        self.clear()
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
