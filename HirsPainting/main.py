from turtle import Turtle, Screen
import random
import colorgram
import os


def get_rgb_colors_from_image() -> list[tuple]:
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, 'image.jpg')

    colors = colorgram.extract(image_path, 10)

    rgb_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors


def draw_hirs_painting(turtle: Turtle, colors_list: list[tuple]):
    x_position = turtle.pos()[0]
    y_position = turtle.pos()[1]

    for i in range(8):
        for j in range(8):
            random_color = random.choice(colors_list)
            color_string = "#{:02x}{:02x}{:02x}".format(*random_color)
            turtle.dot(20, color_string)
            turtle.forward(50)
        y_position += 50
        turtle.setposition(x_position, y_position)


def start():
    turtle_buddy = Turtle()
    turtle_buddy.penup()
    turtle_buddy.setposition(-200, -200)

    colors_list = get_rgb_colors_from_image()
    draw_hirs_painting(turtle_buddy, colors_list)

    screen = Screen()
    screen.exitonclick()
