from .product import Product


class Winkelmandje:
    def __init__(self):
        self.items = []  # lijst van (product, aantal)

    def voeg_toe(self, product, aantal):
        if not product.is_op_voorraad(aantal):
            print("Niet genoeg voorraad")
            return

        product.verlaag_voorraad(aantal)
        self.items.append((product, aantal))
        print("Toegevoegd aan mandje")

    def totaal_prijs(self):
        totaal = 0
        for product, aantal in self.items:
            totaal += product.prijs * aantal
        return totaal

    def toon(self):
        if not self.items:
            print("Mandje is leeg")
            return

        for product, aantal in self.items:
            print(f"{product.naam} x{aantal} = €{product.prijs * aantal}")

        print(f"Totaal: €{self.totaal_prijs()}")