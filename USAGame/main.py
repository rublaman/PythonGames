from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
turtle = Turtle()

screen.title("U.S. States Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

df = pd.read_csv('50_states.csv')

is_game_on = True
guessed_states = []


while is_game_on or len(guessed_states) < 50:
    answer_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states name?").title()
    state_with_cords = df[df["state"] == answer_input]

    if not state_with_cords.empty:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_with_cords.iloc[0]["x"]), int(state_with_cords.iloc[0]["y"]))
        t.write(state_with_cords.iloc[0]["state"])
        guessed_states.append(state_with_cords.iloc[0]["state"])

    if answer_input == "Exit":
        is_game_on = False
