'''
Lawrence Woods
Homework #1.18b
'''

import turtle


s = turtle.Screen()
t = turtle.Turtle()

def Coordinate_System(t, size, num, angle):

    for i in range(num):
        for x in range(1):
            turtle.goto(0, 5)
            turtle.forward(size)
            turtle.left(180)
        turtle.right(90)

Coordinate_System(t, 100, 4, 20)


'''
Lawrence Woods
Homework #1.18b
'''


def draw_quadrant():
    turtle.penup()
    window = turtle.Screen()
    larry= turtle.Turtle()
    larry.forward(100)
    larry.left(120)
    larry.forward(100)
    larry.left(120)
    larry.forward(100)

    window.exitonclick() #to exit

draw_quadrant()