# UNVOLLSTÄNDIGES BEISPIEL

import turtle

# Hintergrundfarbe setzen
turtle.bgcolor("skyblue")

# Haus zeichnen
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.color("black", "lightgrey")
turtle.begin_fill()
for i in range(4):
    turtle.forward(200)
    turtle.right(90)
turtle.end_fill()

# Dach zeichnen
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.color("black", "brown")
turtle.begin_fill()
turtle.goto(0, 200)
turtle.goto(100, 100)
turtle.goto(-100, 100)
turtle.end_fill()

input("Beenden mit <ENTER>")
