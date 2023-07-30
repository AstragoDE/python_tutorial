einkaufsliste = {}

modus = 1

while True:
    if modus == 0:
        exit()

    while modus == 1:
        print("Eingabemodus")

        produkt = input("Produktname: ")
        menge = int(input("Menge: "))

        einkaufsliste[produkt] = menge

        modus = int(input("Ausgabemodus (2) oder Programm beenden (0): "))

    while modus == 2:
        print("Ausgabemodus")

        for produkt, menge in einkaufsliste.items():
            print(produkt + ": " + str(menge))

        modus = int(input("Eingabemodus (1) oder Programm beenden (0): "))
