---
layout: section
---

# Eingaben und Ausgaben

---

# Eingaben und Ausgaben

- Mit dem `input()`-Befehl kann der Computer eingaben entgegennehmen.
- i.d.R wird der `input()`-Befehl mit einer Variable verbunden, welche die Eingabe dann zur weiteren Verwendung speichert.
- Der `input()`-Befehl gibt **immer** einen String zurück, auch wenn man nur Ziffern eingibt.
- Das Programm wird solange _pausiert_ bis der Benutzer seine eingabe mit <kbd>Enter</kbd> bestätigt.

## Beispiel:

```python {all|1|all}
eingabe = input()
print("Du hast folgendes eingegeben: " + eingabe)
```

---

# Aufgabe 1:

Schreibe ein Programm, welches den Benutzer nach seinem Namen fragt, und diesen begrüßt.

## Hinweise:

- Du kannst im `input()`-Befehl auch einen String angeben, der vorher ausgegeben werden soll.

```python
eingabe = input("Dein Alter: ")
```

- Du kannst _formatierte Strings_ (F-Strings) verwenden, um eine Variable im Text auszugeben. Diese muss dann auch nicht konvertiert werden.

```python {2}
eingabe = input("Dein Alter: ")
print(f"Horst ist {eingabe} Jahre alt.")
```

---

# Aufgabe 2

Schreibe ein Programm, welches zwei Ziffern entgegennimmt, diese addiert und im Anschluss ausgibt.

_Hinweis:_

- Um einen String in eine Zahl zu konvertieren, kann man die folgenden Funktionen nutzen:

```python
eingabe = "3"
mein_float = float(eingabe) # Konvertiert String zu Kommazahl
mein_int = int(eingabe) # Konvertiert String zu Ganzzahl
```
