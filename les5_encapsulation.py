# les5_encapsulation.py

class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self._leeftijd = leeftijd  # protected attribuut

    # Getter
    def get_leeftijd(self):
        return self._leeftijd

    # Setter met validatie
    def set_leeftijd(self, nieuwe_leeftijd):
        if nieuwe_leeftijd < 0:
            print("Leeftijd mag niet negatief zijn!")
            return
        if nieuwe_leeftijd > 130:
            print("Leeftijd mag niet hoger zijn dan 130!")
            return
        self._leeftijd = nieuwe_leeftijd

    # Oefening 2: verjaar()
    def verjaar(self):
        huidige_leeftijd = self.get_leeftijd()
        nieuwe_leeftijd = huidige_leeftijd + 1
        self.set_leeftijd(nieuwe_leeftijd)


# ======================
# Testcode
# ======================

s1 = Student("Ali", 19)

print(s1.get_leeftijd())   # 19

s1.set_leeftijd(20)
print(s1.get_leeftijd())   # 20

s1.set_leeftijd(-5)        # foutmelding
print(s1.get_leeftijd())   # blijft 20

s1.set_leeftijd(150)       # foutmelding
print(s1.get_leeftijd())   # blijft 20

s1.verjaar()
print(s1.get_leeftijd())   # 21