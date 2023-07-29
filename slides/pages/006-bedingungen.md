---
layout: section
---

# Bedingungen

---

# Bedingungen

- Bedingungen sind eine Möglichkeit, um den Programmablauf basierend auf vorhandenen Daten zu steuern.
- Je nachdem, ob eine Bedingung erfüllt ist oder nicht, wird ein anderer Programmteil ausgeführt.
- Es gibt 3 verschiedene Bedingungen:
  - `if`-Bedingung
  - `elif`-Bedingung
  - `else`-Bedingung
- Eine Bedingung besteht immer aus einer Bedingung und einem eingerückten Code-Block, der ausgeführt wird, wenn die Bedingung erfüllt ist.
- Eine Bedingung ist erfüllt, wenn das Ergebnis der Vergleichsoperation `True` ist.

---

# Vergleichsoperationen

| Operator | Beschreibung           | Beispiel    |
|----------|------------------------|-------------|
| ==       | Gleich                 | 5 == 5      |
| !=       | Nicht gleich           | 5 != 3      |
| >        | Größer als             | 10 > 5      |
| <        | Kleiner als            | 3 < 7       |
| >=       | Größer oder gleich     | 8 >= 8      |
| <=       | Kleiner oder gleich    | 4 <= 6      |

Alle Vergleichsoperationen geben entweder `True` oder `False` zurück.

--- 

# Die `if`-Bedingung

- Die `if`-Bedingung ist die einfachste Bedingung.
- Sie wird immer dann ausgeführt, wenn die Bedingung erfüllt ist.

## Beispiele:

```python
if 5 > 3:
    print("5 ist größer als 3")
```

```python {2-3}
name = input("Dein Name: ")
if name == "Manfred":
    print("Hallo Manfred! Schön dich zu sehen!")
```

--- 

# Die `elif`-Bedingung

- Die `elif`-Bedingung ist eine Erweiterung der `if`-Bedingung.
- `elif` steht für *else if*, also *sonst wenn*.
- Sie wird immer dann ausgeführt, wenn die Bedingung erfüllt ist, die vorherige jedoch nicht.
- Man kann sie beliebig oft hintereinander verwenden.

```python {4-5}
name = input("Dein Name: ")
if name == "Uwe":
    print("Hallo Uwe! Schön dich zu sehen!")
elif name == "Peter":
    print("Hallo Peter! Schön dich zu sehen!")
```

---

# Die `else`-Bedingung

- Die `else`-Bedingung ist eine Bedingung, welche immer dann ausgeführt wird, wenn keine der vorherigen Bedingungen erfüllt ist.

```python {6-7|2-7}
name = input("Dein Name: ")
if name == "Uwe":
    print("Hallo Uwe! Schön dich zu sehen!")
elif name == "Peter":
    print("Hallo Peter! Schön dich zu sehen!")
else:
    print("Hallo Unbekannter! Schön dich zu sehen!")
```

# Aufgabe 1

Schreibe eine Programm, welches den Benutzer nach seinem Alter fragt und dann ausgibt, ob er volljährig ist oder nicht.

**Hinweis:**
Achte darauf, den String der Input-Funktion in eine Zahl umzuwandeln.

---

# Verknüpfung und Verschachtelung von Bedingungen

- Bedingungen können miteinander verknüpft werden.
- Dafür gibt es die Operatoren `and` und `or`.
- Mehrere Bedingungen können auch verschachtelt werden.

## Beispiel -  Verknüpfung:

```python
name = input("Dein Name: ")
if name == "Uwe" or name == "Peter":
    print("Hallo Uwe oder Peter! Schön euch zu sehen!")
```

## Beispiel -  Verschachtelung:

```python
name = input("Dein Name: ")
alter = int(input("Dein Alter: "))
if name == "Uwe":
    if alter >= 18:
        print("Hallo Uwe! Schön dich zu sehen!")
    else:
        print("Hallo Uwe! Du bist leider noch nicht volljährig!")
```

---

# Aufgabe 2

- Schreibe ein Programm, welches den Benutzer nach seinem Namen und seinem Alter fragt.
- Wenn der Benutzer Uwe heißt und 33 Jahre alt ist, soll das Programm "Hallo Uwe!" ausgeben.
- Wenn der Benutzer Peter heißt, soll das Programm nach seiner Pin fragen.
  - ist Peters Pin 1234, soll das Programm "Hallo Peter!" ausgeben.
  - ist Peters Pin nicht 1234, soll das Programm "Falsche Pin!" ausgeben.
- wenn der Benutzer weder Uwe noch Peter heißt, soll das Programm "Hallo Unbekannter!" ausgeben.