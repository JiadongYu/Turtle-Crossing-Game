import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Crossy Turtle')
screen.listen()

character = Player()
screen.onkey(character.moveup, 'Up')
scoreboard = Scoreboard()

game_is_on = True
loop_counter = 0

car_boss = CarManager()

sleeptime = 0.1

while game_is_on:
    time.sleep(sleeptime)
    screen.update()
    if loop_counter % 6 ==0:
        car_boss.generate_car()
        car_boss.move_car()

    loop_counter += 1
# Detect collisions with cars:
    for car in car_boss.vehicle_list:
        if character.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()
# Detect successful crossing:
    if character.atfinishline():
        character.startingline()
        car_boss.level_up()
        scoreboard.update_score()



screen.exitonclick()
