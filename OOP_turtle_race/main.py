# from turtle import Turtle
import turtle as t
from OOP_turtle_race.turtle_race import TurtleRace
import random
import threading
import time

print(t.screensize())
colors = ["red", "blue", "yellow"]
yAxis = [150, 120, 90]
turtles = []

for x in range(3):
    turtles.append(TurtleRace(yAxis[x], 0, colors[x], t))

guess = input('sence kim kazanir red? blue? yellow?    ')
winner = ''

def check_if_finish():
    for turtle in turtles:
        if turtle.get_xpos() >= 400:
            return True
        return False

while not check_if_finish():
    for turtle in turtles:
        turtle.race()
        # if ()
if winner == guess:
    print('congrats')


screen = t.Screen()
screen.mainloop()








