from turtle import Turtle, Screen
import pandas
import pandas as pd
import os


def start():
    screen = Screen()
    turtle = Turtle()

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, 'blank_states_img.gif')
    csv_path = os.path.join(current_dir, '50_states.csv')

    screen.title("U.S. States Game")
    screen.addshape(image_path)
    turtle.shape(image_path)

    df = pd.read_csv(csv_path)
    guessed_states = []

    while len(guessed_states) < 50:
        answer_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another states name?").title()
        state_with_cords = df[df["state"] == answer_input]

        if answer_input == "Exit":
            missing_states = [state for state in df.state.to_list() if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

        elif not state_with_cords.empty:
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(state_with_cords.iloc[0]["x"]), int(state_with_cords.iloc[0]["y"]))
            t.write(state_with_cords.iloc[0]["state"])
            guessed_states.append(state_with_cords.iloc[0]["state"])


