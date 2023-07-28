---
layout: section
---

# Lektion 2: Variablen und Datentypen

---

# Was sind Variablen?

- Variablen können Daten speichern
- Enthaltene Daten können im Programm verändert werden
- Man kann sie an Stelle von festgeschriebenen Daten verwenden
- Variablen haben einen Namen, denen ein Wert mit dem Zuweisungsoperator "=" zugewiesen wird.

## Beispiel

**"Hello World" mit festgeschriebenen Werten**
```python
print("Hallo Welt!")
```

**"Hello World" mit Variable**
```python {all|1|2}
nachricht = "Hallo Welt!"
print(nachricht)
```

---

# Datentypen

- Daten haben unterschiedliche Datentypen
  
## Warum?

- Bestimmte Operationen lassen sich nur mit speziellen Datentypen durchführen
  - Multiplikation kann nicht mit Zwichenketten durchgeführt werden
- Unterschiedliche Datentypen brauchen unterschiedlich viel Speicher

---

# Datentypen in Python

| Datentyp | Verwendung| Beispiel |
| ----- | ----- | ----- |
| Integer | Ganzzahlen | 69420 |
| Float | Kommazahlen | 3.14159 |
| Boolean | Wahrheitswerte | True *oder* False |
| String | Zwichenketten | "Hallo Welt!" |

---

# Beispiele

## Beispiel 1: Addition von 2 Variablen
**Programm:**
```python {1|2|3|5-6|7|all}
zahl_a = 5
zahl_b = 8
summe = zahl_a + zahl_b

print(zahl_a)
print(zahl_b)
print(summe)
```

**Ausgabe:**
```
5
8
13
```

---

# Beispiele

## Beispiel 2: Zusammenfügen von Strings
**Programm:**
```python 
begruessung = "Hallo, "
name = "Olaf"
text = begruessung + " " + name

print(begruessung)
print(name)
print(text)
```

**Ausgabe:**
```
Hallo,
Olaf
Hallo, Olaf
```

---

# Beispiele

## Beispiel 3: Ein Fehler
**Programm:**
```python 
begruessung = "Hallo, "
name = "Olaf"
text = begruessung / " " + name

print(begruessung)
print(name)
print(text)
```

**Ausgabe:**
```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    text = begruessung / " " + name
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

--- 

# Aufgaben

## Aufgabe 1

Erstelle folgende Variablen:

- *name* mit dem Namen Robert
- *alter* mit einem beliebigen Alter (Ganzzahl)
- *groesse* mit mit einer beliebigen Kommazahl
- *istProgrammierer* mit einem Wahrheitswert

## Aufgabe 2

**WORK IN PROGRESS**