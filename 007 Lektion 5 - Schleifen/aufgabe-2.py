for i in range(1, 101):
    ausgabe = ""

    if i % 3 == 0:
        ausgabe += "Fizz"
    if i % 5 == 0:
        ausgabe += "Buzz"

    if i % 3 != 0 and i % 5 != 0:
        ausgabe += str(i)

    print(ausgabe)
