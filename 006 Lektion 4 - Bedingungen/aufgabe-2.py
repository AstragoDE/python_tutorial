name = input("Wie ist dein Name?: ")
alter = int(input("Wie alt bist du?: "))

if name == "Olaf" and alter == 33:
    print("Hallo Olaf!")
elif name == "Peter":
    pin = int(input("Bitte gib deine PIN ein: "))
    if pin == 1234:
        print("Hallo Peter!")
    else:
        print("Falsche Pin!")
else:
    print("Hallo Unbekannter!")
