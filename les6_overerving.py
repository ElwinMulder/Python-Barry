# les6_overerving.py

# ======================
# Parent class
# ======================
class Persoon:
    def __init__(self, naam):
        self.naam = naam

    def voorstel(self):
        print(f"Ik ben {self.naam}.")


# ======================
# Child class: Student
# ======================
class Student(Persoon):
    def __init__(self, naam, leeftijd, opleiding):
        super().__init__(naam)   # naam komt uit Persoon
        self.leeftijd = leeftijd
        self.opleiding = opleiding

    # override
    def voorstel(self):
        print(f"Ik ben {self.naam}, {self.leeftijd} jaar, opleiding: {self.opleiding}.")


# ======================
# Child class: Docent
# ======================
class Docent(Persoon):
    def __init__(self, naam, vak):
        super().__init__(naam)
        self.vak = vak

    # override
    def voorstel(self):
        print(f"Ik ben {self.naam} en ik geef {self.vak}.")


# ======================
# Testcode
# ======================
s1 = Student("Sara", 20, "Software Development")
d1 = Docent("Ali", "Python")

s1.voorstel()
d1.voorstel()