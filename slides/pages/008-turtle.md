---
layout: section
---

# Python Turtle
## Zeichnen mit Python

---

# Was ist Python Turtle?

- Python Turtle ist ein Modul, das es erlaubt, mit Python zu zeichnen
  - Modul: Enthält code, der in anderen Programmen widerverwendet werden kann

Beispiel:

```python
import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

input("Beenden mit <ENTER>") # Wartet auf Eingabe, damit das Fenster nicht sofort geschlossen wird
```

---

# Befehele von Python Turtle 1

| Befehl              | Beschreibung                                    |
|---------------------|-------------------------------------------------|
| `import turtle`     | Importiere das Turtle-Modul.                    |
| `forward(distance)` | Bewegt die Turtle vorwärts um die angegebene Entfernung. |
| `backward(distance)`| Bewegt die Turtle rückwärts um die angegebene Entfernung. |
| `right(angle)`      | Dreht die Turtle nach rechts um den angegebenen Winkel.    |
| `left(angle)`       | Dreht die Turtle nach links um den angegebenen Winkel.     |
| `penup()`           | Hebt den Stift der Turtle an, sodass sie ohne zu zeichnen bewegt werden kann. |
| `pendown()`         | Senkt den Stift der Turtle, sodass sie beim Bewegen zeichnet.    |


---


# Befehele von Python Turtle 2

| Befehl              | Beschreibung                                    |
|---------------------|-------------------------------------------------|
| `speed(speed)`      | Legt die Zeichengeschwindigkeit der Turtle fest (1 = langsamste, 10 = schnellste). |
| `color(color)`      | Ändert die Farbe des Stifts oder der Füllung.        |
| `pensize(width)`    | Legt die Breite des Stifts fest.                   |
| `fillcolor(color)`  | Legt die Farbe für die Füllung von Formen fest.    |
| `begin_fill()`      | Beginnt das Ausfüllen einer Form.                 |
| `end_fill()`        | Beendet das Ausfüllen einer Form.                 |


---

# Befehele von Python Turtle 3

| Befehl              | Beschreibung                                    |
|---------------------|-------------------------------------------------|
| `circle(radius)`    | Zeichnet einen Kreis mit dem angegebenen Radius.  |
| `dot(size)`         | Zeichnet einen Punkt mit der angegebenen Größe.   |
| `goto(x, y)`        | Bewegt die Turtle zum angegebenen Punkt (x, y) ohne zu zeichnen. |
| `clear()`           | Löscht das Zeichenfenster und setzt die Turtle zurück.      |

---

# Aufgaben

## Aufgabe 1

- Zeichne ein Quadrat mit einer vom Benutzer eingegebenen Seitenlänge.
- Optimiere dein Programm so, dass es möglichst wenig Code enthält.
  - Verwende dazu Schleifen.

## Aufgabe 2

- Schreibe ein Programm, welches ein Bild deiner Wahl zeichnet.
- Verwende verschiedene Farben und Formen.