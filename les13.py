class Product:
    def __init__(self, naam, prijs):
        self.naam = naam
        self.prijs = prijs


# 🏭 Factory Pattern
class ProductFactory:
    def maak_product(self, soort):
        soort = soort.lower()

        if soort == "laptop":
            return Product("Laptop", 899)
        elif soort == "muis":
            return Product("Muis", 25)
        elif soort == "toetsenbord":
            return Product("Toetsenbord", 59)
        else:
            raise ValueError(f"Onbekend product: {soort}")


# 🎯 Strategy Pattern (korting regels)
class KortingRegel:
    def pas_toe(self, totaal):
        raise NotImplementedError


class GeenKorting(KortingRegel):
    def pas_toe(self, totaal):
        return 0


class TienProcentBoven500(KortingRegel):
    def pas_toe(self, totaal):
        if totaal > 500:
            return totaal * 0.10
        return 0


# 🧾 Kassa
class Kassa:
    def __init__(self, korting_regel):
        self.producten = []
        self.korting_regel = korting_regel

    def voeg_toe(self, product):
        self.producten.append(product)

    def totaal(self):
        return sum(p.prijs for p in self.producten)

    def korting(self):
        return self.korting_regel.pas_toe(self.totaal())

    def eindbedrag(self):
        return self.totaal() - self.korting()