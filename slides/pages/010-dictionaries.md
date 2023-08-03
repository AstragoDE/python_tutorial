---
layout: section
---

# Lektion 7: Dictionaries

## (Wörterbücher)

---

# Dictionaries

- Dictionaries sind eine Sammlung von Werten
- Dictionaries können Werte von verschiedenen Datentypen enthalten
- Dictionaries können Werte mehrfach enthalten
- Jedes Element in einem Dictionary hat einen Schlüssel (Key) und einen Wert (Value)
  - Der Schlüssel ist eindeutig und kann nicht mehrfach vorkommen
  - Der Wert kann mehrfach vorkommen

---

# Dictionaries - Beispiele

## Beispiel 1

```python
einkaufsliste = {
    "Milch": 1,
    "Eier": 6,
    "Brot": 2,
    "Käse": 1
}

milch_menge = einkaufsliste["Milch"] # speichert den Wert von "Milch" in der Variable milch_menge
print(milch_menge)

print(einkaufsliste["Brot"]) # gibt den Wert von "Brot" aus
```

**Ausgabe:**

```
1
2
```

---

# Dictionaries - Beispiele

## Elemente hinzufügen und entfernen

```python
einkaufsliste = {
    "Milch": 1,
    "Eier": 6,
    "Brot": 2,
    "Käse": 1
}

einkaufsliste["Wurst"] = 2 # fügt ein Element mit dem Schlüssel "Wurst" und dem Wert 2 hinzu

print(einkaufsliste)

einkaufsliste.pop("Eier") # entfernt das Element mit dem Schlüssel "Eier"

print(einkaufsliste)
```

**Ausgabe:**

```
{'Milch': 1, 'Eier': 6, 'Brot': 2, 'Käse': 1, 'Wurst': 2}
{'Milch': 1, 'Brot': 2, 'Käse': 1, 'Wurst': 2}
```

---

# Dictionaries - Beispiele

## For-Schleife mit Schlüssel und Wert

```python
einkaufsliste = {
    "Milch": 1,
    "Eier": 6,
    "Brot": 2,
    "Käse": 1
}

for key, value in einkaufsliste.items():
    print(f"{key} --> {value}")
```

**Ausgabe:**

```
Milch -> 1
Eier -> 6
Brot -> 2
Käse -> 1
```

---

# Aufgabe

Erstelle ein Programm, welches eine Einkaufsliste erstellen kann, indem es den Benutzer nach dem Namen und der Menge eines Produktes fragt. Baue eine Funktion ein, welche die Einkaufsliste ausgibt.
