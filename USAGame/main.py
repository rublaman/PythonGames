from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

screen.title("U.S. States Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

answer_input = screen.textinput(title="Guess the State", prompt="What's another states name?")
