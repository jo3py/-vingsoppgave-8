import turtle
import math

t = turtle.Turtle()
farger = ["grey", "blue", "grey", "blue"]
side = 10
angel = 0
turtle.speed(1000)
for turn in range(1, 40):
    hypotenus = math.sqrt(side**2 + side**2)
    t.penup()
    t.home()
    t.right(180)
    t.right(45 + angel)
    t.forward(hypotenus/2)
    t.right(135)
    t.pendown()
    for firkant in range(0, 4):
        t.color(farger[firkant])
        t.width(2)
        t.forward(side)
        t.right(90)
    side += 10
    angel += 8
turtle.done()