from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.list_of_cars: list[Turtle] = []
        self.create_list_of_cars()
        self.speed = STARTING_MOVE_DISTANCE

    def create_list_of_cars(self):
        for _ in range(0, 15):
            self.add_car()

    def add_car(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(random.randint(300, 1000), random.randint(-250, 250))
        self.list_of_cars.append(car)

    def move(self):
        for car in self.list_of_cars:
            car.forward(self.speed)

            if car.xcor() < -300:
                car.goto(300, random.randint(-250, 250))

    def increment_speed(self):
        self.speed += MOVE_INCREMENT
