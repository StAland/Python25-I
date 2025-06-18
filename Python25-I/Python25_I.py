
# - - - Infos / Bücher / Links - - - - - - - - - - - - - - - - - - - - - - - - -

# Buch  Programmieren mit Python (westermann)  Kapitel 7.5  Abstrakte Klassen und Interfaces
# Link  https://www.datacamp.com/de/tutorial/python-abstract-classes


# - - - Definitionen - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from abc import ABC, abstractmethod

# 'Tier' ist eine abstrakte Klasse, weil:
# - erbt von ABC
# - eine abstrakte Methode enthält (@abstractmethod)
class Tier(ABC):
    def __init__(self, farbe):
        self.__farbe = farbe

    @abstractmethod
    def mach_geraeusch(self):
        print("Das Tier macht Geräusche.")
    
    def hallo(self):
        print("Hallo, ich bin ein Tier.")

# 'Hund' ist eine reguläre Klasse.
# Da diese von der abstrakten 'Tier' erbt, muss 'Hund' die
# abstrakte Methode 'mach_geraeusch()' implmentieren.
class Hund(Tier):
    def mach_geraeusch(self):
        super().mach_geraeusch()
        print("Der Hund bellt.")

class Katze(Tier):
    def mach_geraeusch(self):
        print("Die Katze miaut.")
    
    def hallo(self):
        print("Hallo, ich bin eine Katze.")

class Maus(Tier):
    def mach_geraeusch(self):
        print("Die Maus piept.")

# - - - Test-Code / Demonstration  - - - - - - - - - - - - - - - - - - - - - - -

def main():
    # tier = Tier()     # wirft einen Fehler, da Instanzen von abstrakten Klassen nicht erlaubt sind
    hund = Hund("weiß")
    katze = Katze("schwarz")
    maus = Maus("grau")

    hund.mach_geraeusch()
    hund.hallo()
    
    katze.mach_geraeusch()
    katze.hallo()

    maus.mach_geraeusch()

main()
