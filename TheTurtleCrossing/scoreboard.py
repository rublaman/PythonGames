from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-260, 250)
        self.update_scoreboard_text()

    def increase_scoreboard(self):
        self.level += 1
        self.update_scoreboard_text()

    def update_scoreboard_text(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
        self.goto(-80, 0)
        self.write("GAME OVER", font=FONT)
