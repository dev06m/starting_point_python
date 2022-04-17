import turtle
import turtle as t
import random
import time

class TurtleRace:

    def __init__(self, location, speed, color, turtle):
        self.turtle = t.Turtle()
        self.turtle.setpos((0, 0))
        self.turtle.speed(speed)
        self.turtle.color(color)
        self.print_pos(turtle)
        time.sleep(0.2)
        self.set_position((-280, location))

    def gen_ran_num(self):
        return random.randint(0, 100)

    def set_position(self, pos):
        self.turtle.setpos(pos)

    def race(self):
        ran_num = random.randint(0, 10)
        self.turtle.forward(ran_num)
        time.sleep(0.1)

    def get_xpos(self):
        return self.turtle.xcor()

    def print_pos(self, turtle):
        print(turtle.screensize(), self.turtle.xcor())

    def get_color(self):
        return self.turtle.color



