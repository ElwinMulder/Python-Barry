class Student:
    def __init__(self, naam, leeftijd, opleiding):
        self.naam = naam
        self.leeftijd = leeftijd
        self.opleiding = opleiding

    def begroet(self):
        print(
            f"Hallo, ik ben {self.naam}, "
            f"ik ben {self.leeftijd} jaar "
            f"en ik volg de opleiding {self.opleiding}."
        )


# objecten maken
student1 = Student("Ali", 19, "Software Developer")
student2 = Student("Sara", 20, "ICT Beheer")

# methodes aanroepen
student1.begroet()
student2.begroet()
