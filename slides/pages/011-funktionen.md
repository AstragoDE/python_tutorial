---
layout: section
---

# Lektion 8: Funktionen

---

# Funktionen

- Funktionen erlauben es, Code zu kapseln und wiederverwendbar zu machen
- Sie können Parameter entgegennehmen und Werte zurückgeben

- Funktionen müssen definiert werden, bevor sie aufgerufen werden können 
- Funktionen können sich selbst aufrufen (rekursiv)

---

# Beispiele

## Funktion ohne Parameter und Rückgabewert

```python
# Definition einer Funktion
def lorem_ipsum():
    print("Lorem ipsum dolor sit amet")
    print("consectetur adipiscing elit")
    print("sed do eiusmod tempor incididunt ut labore et dolore magna aliqua")

# Aufruf der Funktion
lorem_ipsum()
```

**Ausgabe:**

```
Lorem ipsum dolor sit amet
consectetur adipiscing elit
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
```

---

# Funktion mit Parameter und Rückgabewert

- Die Parameter werden in Klammern hinter dem Funktionsnamen angegeben
  - Die Parameter werden durch Kommas getrennt
  - Sie sind in der Funktion als lokale Variablen verfügbar
- Der Rückgabewert wird mit dem Schlüsselwort `return` zurückgegeben
  - Es kann nur ein Wert zurückgegeben werden
  - Wenn kein Wert zurückgegeben werden soll, kann `return` auch ohne Wert verwendet werden
  - Nach `return` wird die Funktion beendet

---

# Beispiel: Funktion mit Parameter und Rückgabewert

```python
# Definition zweier Funktionen
def addiere(a, b):
    return a + b

def volljaehrig(alter):
    if alter >= 18:
        return True
    return False

# Aufruf der Funktionen
print(addiere(2, 3))
print(volljaehrig(17))
```

---

# Rekursion 

- Eine Funktion kann sich selbst aufrufen

## Beispiel

```python
def countdown(n):
    if n == 0:
        print("Start!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
```

**Ausgabe:**

```
5
4
3
2
1
Start!
```

---

# Aufgabe 

- Schreibe eine Funktion `begruesse(name)`, die den Namen einer Person als Parameter entgegennimmt und sie mit der `print()`-Funktion begrüßt

- Schreibe eine Funktion `ist_kalt()`, die eine Temperatur als Parameter entgegennimmt und `True` zurückgibt, wenn die Temperatur unter 10°C liegt, ansonsten `False`
  - Nutze den Rückgabewert der Funktion, um eine entsprechende Meldung auszugeben