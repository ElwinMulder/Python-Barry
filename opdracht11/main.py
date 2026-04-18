from shop.product import Product
from shop.mandje import Winkelmandje


producten = [
    Product("Laptop", 899, 3),
    Product("Muis", 25, 10),
    Product("Toetsenbord", 59, 5)
]

mandje = Winkelmandje()


def toon_producten():
    for i, p in enumerate(producten):
        print(f"{i}: ", end="")
        p.toon_info()


while True:
    print("\n--- Menu ---")
    print("1: Toon producten")
    print("2: Voeg toe aan mandje")
    print("3: Toon mandje")
    print("0: Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        toon_producten()

    elif keuze == "2":
        toon_producten()
        try:
            index = int(input("Kies productnummer: "))
            aantal = int(input("Aantal: "))
            mandje.voeg_toe(producten[index], aantal)
        except (ValueError, IndexError):
            print("Ongeldige invoer")

    elif keuze == "3":
        mandje.toon()

    elif keuze == "0":
        print("Programma gestopt")
        break

    else:
        print("Ongeldige keuze")