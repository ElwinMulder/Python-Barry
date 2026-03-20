# Stap 1: class Student maken
class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    # Stap 5: methode toevoegen
    def is_volwassen(self):
        return self.leeftijd >= 18


# Stap 2: drie student-objecten maken
s1 = Student("Ali", 19)
s2 = Student("Sara", 20)
s3 = Student("Jan", 17)

# Stap 3: studenten in een lijst zetten
studenten = [s1, s2, s3]

# Stap 6: teller voor 18+
aantal_volwassen = 0

# Stap 4 + 5: for-loop gebruiken
for student in studenten:
    print(student.naam, student.leeftijd, "Volwassen:", student.is_volwassen())

    if student.is_volwassen():
        aantal_volwassen += 1

# Stap 6: totaal printen
print("Aantal studenten 18+:", aantal_volwassen)
