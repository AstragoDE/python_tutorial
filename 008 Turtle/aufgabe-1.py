import turtle

# Benutzereingabe für die Seitenlänge
seitenlaenge = int(input("Gib die Seitenlänge des Quadrats ein: "))

# Schleife zum Zeichnen des Quadrats
for i in range(4):
    turtle.forward(seitenlaenge)
    turtle.right(90)

input("Beenden mit <ENTER>")
