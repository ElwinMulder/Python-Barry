from abc import ABC, abstractmethod # zorgt ervoor dat we een abstracte class kunnen maken en 
# elke subclass de betaal methode moet implementeren


# Abstracte class
class Betaalmethode(ABC):

    def __init__(self, naam):
        self.naam = naam

    @abstractmethod
    def betaal(self, bedrag):
        pass


# Subclass 1
class PinBetaling(Betaalmethode):

    def __init__(self):
        super().__init__("Pin")

    def betaal(self, bedrag):
        return f"{self.naam} betaling: €{bedrag} is gepind."


# Subclass 2
class ContantBetaling(Betaalmethode):

    def __init__(self):
        super().__init__("Contant")

    def betaal(self, bedrag):
        return f"{self.naam} betaling: €{bedrag} contant ontvangen."


# Subclass 3
class OnlineBetaling(Betaalmethode):

    def __init__(self):
        super().__init__("Online")

    def betaal(self, bedrag):
        return f"{self.naam} betaling: €{bedrag} online verwerkt."


# Testen met een lijst
methodes = [
    PinBetaling(),
    ContantBetaling(),
    OnlineBetaling()
]

for methode in methodes:
    print(methode.betaal(49.95))