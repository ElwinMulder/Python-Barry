# Stap 2 — Class Student maken
class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def begroet(self):
        print(f"Hallo, ik ben {self.naam}!")


# Stap 3 — Lijst met studenten (minimaal 3)
studenten = [
    Student("Ali", 19),
    Student("Sara", 20),
    Student("Jan", 18),
]

# Stap 4 — Loop door de lijst en roep begroet() aan
for s in studenten:
    s.begroet()

print()  # lege regel voor overzicht

# Oefening deel 1 — Tel hoeveel studenten 18+ zijn
aantal_18_plus = 0

for s in studenten:
    if s.leeftijd >= 18:
        aantal_18_plus += 1

print("Aantal studenten 18+:", aantal_18_plus)

# Oefening deel 2 — Gemiddelde leeftijd berekenen
totaal_leeftijd = 0

for s in studenten:
    totaal_leeftijd += s.leeftijd

gemiddelde = totaal_leeftijd / len(studenten)

print("Gemiddelde leeftijd:", gemiddelde)
