def begruessung(name):
    print(f"Hallo {name}")


def ist_kalt(temperatur):
    if temperatur < 10:
        return True
    return False


begruessung("Horst-Günter")

temperatur = int(input("Welche Temperatur wurde gemessen?: "))

if ist_kalt(temperatur):
    print("Es ist kalt.")
else:
    print("Es ist nicht kalt.")
