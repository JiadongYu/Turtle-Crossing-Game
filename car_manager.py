from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager():
    def __init__(self):
        self.vehicle_list = []
        self.carspeed = MOVE_INCREMENT

    def generate_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_wid=1, stretch_len= 2)
        new_car.penup()
        possible_y_coordinates = random.randint(-250,250)
        random_color = random.choice(COLORS)
        new_car.color(random_color)
        new_car.goto(300,possible_y_coordinates)
        new_car.setheading(180)
        self.vehicle_list.append(new_car)


    def move_car(self):
        for car in self.vehicle_list:
            car.forward(self.carspeed)

    def level_up(self):
        self.carspeed += 10

