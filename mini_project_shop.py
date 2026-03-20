class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def toon_info(self):
        print(f"{self.naam} - €{self.prijs} (voorraad: {self._voorraad})")

    def is_op_voorraad(self):
        return self._voorraad > 0

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            print("Aantal moet groter dan 0 zijn.")
            return False

        if self._voorraad < aantal:
            print("Niet genoeg voorraad.")
            return False

        self._voorraad -= aantal
        return True


class Winkelmandje:
    def __init__(self):
        self.items = []

    def voeg_toe(self, product):
        self.items.append(product)
        print(f"Toegevoegd: {product.naam}")

    def toon_mandje(self):
        if not self.items:
            print("Mandje is leeg.")
            return

        print("\nProducten in mandje:")
        for item in self.items:
            print(f"- {item.naam} (€{item.prijs})")

    def totaal_prijs(self):
        totaal = 0
        for item in self.items:
            totaal += item.prijs
        return totaal


# Startproducten
producten = [
    Product("Laptop", 899, 3),
    Product("Muis", 25, 10),
    Product("Toetsenbord", 59, 5),
]

mandje = Winkelmandje()


# Menu
while True:

    print("\n--- Mini Webshop ---")
    print("1 = Producten bekijken")
    print("2 = Product toevoegen")
    print("3 = Mandje bekijken")
    print("4 = Afrekenen")
    print("0 = Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        print("\nBeschikbare producten:")
        for i, product in enumerate(producten):
            print(f"{i}. ", end="")
            product.toon_info()

    elif keuze == "2":
        try:
            nummer = int(input("Kies productnummer: "))
            if 0 <= nummer < len(producten):
                product = producten[nummer]
                mandje.voeg_toe(product)
            else:
                print("Ongeldig productnummer.")
        except ValueError:
            print("Voer een geldig nummer in.")

    elif keuze == "3":
        mandje.toon_mandje()
        print(f"Totaal: €{mandje.totaal_prijs()}")

    elif keuze == "4":
        if not mandje.items:
            print("Je mandje is leeg.")
            continue

        alles_gelukt = True

        for item in mandje.items:
            if not item.verlaag_voorraad(1):
                alles_gelukt = False
                break

        if alles_gelukt:
            print("Bedankt voor je aankoop!")
            mandje.items = []
        else:
            print("Afrekenen mislukt door voorraadprobleem.")

    elif keuze == "0":
        print("Programma gestopt.")
        break

    else:
        print("Ongeldige keuze.")
