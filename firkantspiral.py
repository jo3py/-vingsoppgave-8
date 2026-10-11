import turtle
import math

t = turtle.Turtle()
farger = ["red", "yellow", "green", "blue"]
side = 10
vinkel = 20
fremover = 5
angel = 7
halvside = 0
t.penup()
t.home()
t.right(180)
t.forward(side/2)
t.right(90)
t.forward(side/2)
t.pendown()
t.right(90)
for firkant in range(0, 4):
    t.penup()
    t.forward(side)
    t.right(90)
for teller in range(1, 51):
    side += 5
    t.penup()
    t.home()
    t.right(180 + angel)
    t.forward(fremover)
    t.right(90 + angel)
    t.forward(fremover)
    t.pendown()
    t.right(90 + angel)
    #t.right(vinkel)
    vinkel += 5
    fremover += 5
    angel += 7
    for firkant in range(0, 4):
        t.color(farger[firkant])
        t.width(2)
        t.forward(side)
        t.right(90)

turtle.done()