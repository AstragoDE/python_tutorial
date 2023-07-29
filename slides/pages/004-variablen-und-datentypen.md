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
name = "Uwe"
text = begruessung + " " + name

print(begruessung)
print(name)
print(text)
```

**Ausgabe:**
```
Hallo,
Uwe
Hallo, Uwe
```

---

# Beispiele

## Beispiel 3: Ein Fehler
**Programm:**
```python 
begruessung = "Hallo, "
name = "Uwe"
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
- *groesse* mit der größe von 181 cm in m (Kommazahl)
- *istProgrammierer* mit einem Wahrheitswert

Beachte, dass Kommazahlen in Python mit einem Punkt statt einem Komma angegeben werden.

---

# Aufgaben

## Aufgabe 2

1. Gib die Variablen mit dem `print()` befehl aus.
1. Gib mindestens 2 Variablem in einem Print Befehl aus.

**Tipp:**
Um Variablen eines unterschiedlichen Typs in einem Print-Befehl auszugeben, muss man sie mit dem `str(WERT)` Befehl in einen String konvertieren.

<v-click>

*Besispiel:*

```python
alter = 25
print("Uwe ist " + str(alter) + " Jahre alt.")
```

</v-click>


---

# Aufgaben

## Aufgabe 3

- Verändere einige Variablen unter der Ausgabe und gib sie erneut aus.
