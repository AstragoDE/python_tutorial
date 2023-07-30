---
layout: section
---

# Schleifen

---

# Schleifen

- Schleifen erlauben es, Code mehrfach auszuführen
- Es gibt zwei Arten von Schleifen:
  - `while`-Schleifen
  - `for`-Schleifen
- Ähnlich wie bei Bedingungen wird der Code in Schleifen durch Einrückung gekennzeichnet

---

# Die `while`-Schleife

- Die `while`-Schleife führt den Code in ihrem Rumpf so lange aus, wie die Bedingung (oben) wahr ist

## Beispiel:

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

`i += 1` ist eine Kurzform für `i = i + 1`

**Ausgabe:**

```
0
1
2
3
4
5
6
7
8
9
```

---

# Die `for`-Schleife

- Die `for`-Schleife führt den Code in ihrem Rumpf für jedes Element in einer Liste aus
  - --> _Listen folgen später_
- Bei jedem Durchlauf wird das aktuelle Element in der Variablen `i` gespeichert

## Beispiel:

```python
for i in range(10):
    print(i)
```

**Ausgabe:**

```
0
1
2
3
4
5
6
7
8
9
```

`range(10)` ist eine Funktion, die eine Liste mit den Zahlen von 0 bis 9 zurückgibt.

---

# `break` und `continue`

- Mit `break` kann eine Schleife vorzeitig beendet werden
- Mit `continue` kann ein Durchlauf der Schleife vorzeitig beendet werden. Die Schleife wird dann mit dem nächsten Element fortgesetzt.

```python
for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
```

**Ausgabe:**

```
0
1
2
3
4
6
7
```

---

# Aufgaben

## Aufgabe 1

- Schreibe ein Programm, das die Zahlen von 1 bis 100 ausgibt.

**Hinweis:**
Der `range`-Befehl kann auch mit zwei Parametern aufgerufen werden, z.B. `range(1, 10)`. Dann wird eine Liste mit den Zahlen von 1 bis 9 zurückgegeben.

## Aufgabe 2

Schreibe ein Programm, das die Zahlen von 1 bis 100 ausgibt, aber alle Zahlen, die durch 3 teilbar sind, durch "Fizz" ersetzt und alle Zahlen, die durch 5 teilbar sind, durch "Buzz" ersetzt.
Wenn eine Zahl durch 3 und 5 teilbar ist, soll "FizzBuzz" ausgegeben werden.

**Hinweis:**
Der Modulo-Operator `%` gibt den Rest einer Division zurück. `10 % 3` ist also 1.
