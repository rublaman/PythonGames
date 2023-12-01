from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

screen.title("U.S. States Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)


def get_mouse_click_coor(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()
