import turtle
import math

t = turtle.Turtle()
farger = ["red", "yellow", "green", "blue"]
side = 15
vinkel = 30
fremover = 5
t.penup()
t.right(180)
t.forward(side/2)
t.pendown()
t.right(180)
for teller in range(1, 51):
    for firkant in range(0, 4):
        t.color(farger[firkant])
        t.width(2)
        t.forward(side)
        t.right(90)

    t.right(-90)
    t.penup()
    t.forward(fremover)
    t.pendown()
    t.right(90)

    t.right(15)
  

    #vinkel += (3/teller)
    side += 5
    fremover += 2
    vinkel += 5
turtle.done()