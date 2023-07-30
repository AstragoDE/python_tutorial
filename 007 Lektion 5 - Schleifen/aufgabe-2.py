for i in range(1, 101):
    wort_ausgegeben = False
    ausgabe = ""
    if i % 3 == 0:
        ausgabe += "Fizz"
        wort_ausgegeben = True
    if i % 5 == 0:
        ausgabe += "buzz"
        wort_ausgegeben = True

    if not wort_ausgegeben:
        ausgabe += str(i)

    print(ausgabe)
