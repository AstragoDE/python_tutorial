---
layout: section
---

# Listen

---

# Listen

- Listen sind eine Sammlung von Werten
- Listen können Werte von verschiedenen Datentypen enthalten
- Listen können Werte mehrfach enthalten
- Jedes Element in einer Liste hat eine Position (Index)
  - Der Index beginnt bei 0
- Anwendungsfälle:
  - ToDo-Listen (Aufgaben)
  - Reiseplanung (Koordination von Reisezielen)


Beispiel:

```python
mitarbeiter = ["Uwe", "Peter", "Manfred", "Horst-Günter"] # Liste mit nur Strings
irgendwelche_werte ["Dernbach", 56307, "Rheinland-Pfalz", 5.5, True] # Liste mit verschiedenen Datentypen
```

---

# Listen - Beispiele

## Elemente hinzufügen, entfernen und Listenlänge

```python
meine_liste = ["Uwe", "Peter"]

meine_liste.append("Manfred")  # fügt ein Element am Ende der Liste hinzu
meine_liste.insert(0, "Horst-Günter")  # fügt ein Element an der Stelle 0 ein

print(meine_liste)
print(len(meine_liste))  # gibt die Länge der Liste aus

meine_liste.pop(1)  # entfernt das Element an der Stelle 1

print(meine_liste)
print(len(meine_liste))
```

**Ausgabe:**

```text
['Horst-Günter', 'Uwe', 'Peter', 'Manfred']
['Horst-Günter', 'Peter', 'Manfred']
```

--- 

# Liste - Beispiele

## Ein bestimmtes Element ausgeben

- Die Elemente in einer Liste können über ihren Index angesprochen werden

```python
meine_liste = ["Uwe", "Peter", "Manfred", "Horst-Günter"]

print(meine_liste[0])  # gibt das Element an der Stelle 0 aus

meine_liste[0] = "Mitarbeiter 1"  # überschreibt das Element an der Stelle 0

print(meine_liste[0])
```

**Ausgabe:**

```
Uwe
Mitarbeiter 1
```

---

# Liste - Beispiele

## Elemente mit For-Schleife ausgeben

```python
meine_liste = ["Uwe", "Peter", "Manfred", "Horst-Günter"]

for i in meine_liste:
    print(i)
```

**Ausgabe:**

```
Uwe
Peter
Manfred
Horst-Günter
```

---

# Strings teilen und in Listen umwandeln

- Strings können mit der `split(<TRENNZEICHEN>)`-Methode in Listen umgewandelt werden

## Beispiel

```python
mein_string = "Uwe,Peter,Manfred,Horst-Günter"

meine_liste = mein_string.split(",")  # teilt den String an jedem Komma

print(meine_liste)
```

**Ausgabe:**

```
['Uwe', 'Peter', 'Manfred', 'Horst-Günter']
```

---

# Strings teilen und in Listen umwandeln - Zusatz


Wenn zwischen den Trennzeichen Leerzeichen stehen, werden diese mit in die Liste aufgenommen.
Um Leerzeichen zu entfernen, kann die `strip()`-Methode verwendet werden.

```python
mein_string = "Uwe   , Peter, Manfred ,Horst-Günter"

meine_liste = mein_string.split(",")  # teilt den String an jedem Komma

for i in range(len(meine_liste)):
    meine_liste[i] = meine_liste[i].strip()  # entfernt Leerzeichen am Anfang und Ende

print(meine_liste)
```

**Ausgabe:**

```
['Uwe', 'Peter', 'Manfred', 'Horst-Günter']
```

---

# Aufgaben

## Aufgabe 1

Gegeben ist eine Liste mit den Namen von Mitarbeitern. Schreibe ein Programm, das die Namen der Mitarbeiter ausgibt, die mit "M" beginnen.

```python
mitarbeiter = ["Uwe", "Peter", "Manfred", "Horst-Günter"]
```

**Hinweis:** Wie auch Listen, können Strings mit dem Index angesprochen werden. Jeder Buchstabe hat seinen eigenen Index.

## Aufgabe 2

Gegeben ist die Liste aus Aufgabe 1. Schreibe ein Programm, das eine zweite Liste erstellt, die die Namen der Mitarbeiter in umgekehrter Reihenfolge enthält.

**Tipps:**
- Die `insert(<INDEX>, <ELEMENT>)`-Methode kann verwendet werden, um ein Element an einer bestimmten Stelle in eine Liste einzufügen.

