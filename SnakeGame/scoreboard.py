from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


def read_score_from_file():
    path = "./SnakeGame/data.txt"
    filename = os.path.abspath(path)
    with open(filename, "r") as file:
        return int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_score_from_file()
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            print(f"high score {self.high_score}")
            self.write_new_score_to_file()
        self.score = 0
        self.update_scoreboard()

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()

    def write_new_score_to_file(self):
        path = "./SnakeGame/data.txt"
        filename = os.path.abspath(path)
        with open(filename, "w") as data:
            data.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
