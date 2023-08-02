einkaufsliste = {}

modus = 1

while True:
    if modus == 0:
        exit()

    while modus == 1:
        print("Eingabemodus")
        weitereEingabe = True

        while weitereEingabe:
            produkt = input("Produktname: ")
            menge = int(input("Menge: "))

            weA = input("Weitere eingabe? ")

            einkaufsliste[produkt] = menge

            if weA.capitalize().startswith("J"):
                continue
            else:
                weitereEingabe = False

        modus = int(input("Ausgabemodus (2) oder Programm beenden (0): "))

    while modus == 2:
        print("Ausgabemodus")

        for produkt, menge in einkaufsliste.items():
            print(produkt + ": " + str(menge))

        modus = int(input("Eingabemodus (1) oder Programm beenden (0): "))
