import math
import turtle

#fargeliste = ["red", "yellow", "green", "cyan", "blue", "magenta"]   #-magenta
def mangekant_spiral(fargeliste):
    antall_kanter = len(fargeliste)
    side = 10
    angel = 0
    vinkelC = 360/antall_kanter
    vinkelB = (180-vinkelC)/2

    def lengde_til_b(side, vinkelC, vinkelB):
        b = (side/(math.sin(math.radians(vinkelC)))*(math.sin(math.radians(vinkelB))))
        return b

    turtle.speed(1000)
    t = turtle.Turtle()
    for turn in range(1, 40):

        b = lengde_til_b(side, vinkelC, vinkelB)

        t.penup()
        t.home()
        t.right(180)
        t.right(vinkelC + angel)
        t.forward(b)
        t.right(180-vinkelC)
        t.pendown()
        if antall_kanter >= 3:
            angleP = float(360/antall_kanter)
            for polygon in range(0, antall_kanter):
                t.color(fargeliste[polygon])
                t.width(2)
                t.forward(side)
                t.right(angleP)
        else:
            print("Det må minimum være 3 sider i et polygon! Program avsluttes.")
        side += 14
        angel += 10
    turtle.done()

startverdi = True
fargeliste = []
while startverdi:
    farge = input("Skriv inn en farge: ")
    print(type(farge))
    try:
        farge = float(farge)
        startverdi = False
    except ValueError:
        fargeliste.append(farge)
        startverdi = True

mangekant_spiral(fargeliste)
        

