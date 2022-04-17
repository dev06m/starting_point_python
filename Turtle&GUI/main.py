import random
from turtle import Turtle
import turtle as t

num_sides = 20
colors = []

# def draw_shape(num_sides):
#     for x in range(num_sides):
#         angle = 360 / num_sides # 144
#         t.forward(100)
#         t.right(angle)
#         print(' ')
#
# for x in range(3, 11):
#     t.color(random.choice(['yellow', 'green', 'blue', 'red']))
#     # t.color(random.randint(0, 225))
#     # draw_shape(x)

screen = t .Screen()


def r():
    t.forward(10)


def l():
    t.backward(10)


def u():
    t.right(45)


def d():
    t.left(45)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkey(u, "Up")
screen.onkey(d, "Down")
screen.onkey(r, "Right")
screen.onkey(l, "Left")
screen.onkey(clear, "c")

screen.listen()

screen.mainloop()
