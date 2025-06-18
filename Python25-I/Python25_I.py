
# - - - Infos / Bücher / Links - - - - - - - - - - - - - - - - - - - - - - - - -

# Buch  Programmieren mit Python (westermann)  Kapitel 7.5  Abstrakte Klassen und Interfaces
# Link  https://www.datacamp.com/de/tutorial/python-abstract-classes


# - - - Definitionen - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from abc import ABC, abstractmethod

# 'Tier' ist eine abstrakte Klasse, weil:
# - erbt von ABC
# - eine abstrakte Methode enthält (@abstractmethod)
class Tier(ABC):
    @abstractmethod
    def __init__(self, farbe, alter):
        self.__farbe = farbe
        self.__alter = alter

    @abstractmethod
    def mach_geraeusch(self):
        print("Das Tier macht Geräusche.")
    
    def hallo(self):
        print("Hallo, ich bin", self.__farbe, "und", self.__alter, "Jahre alt.")

# 'Hund' ist eine reguläre Klasse.
# Da diese von der abstrakten 'Tier' erbt, muss 'Hund' die
# abstrakte Methode 'mach_geraeusch()' implmentieren.
class Hund(Tier):
    def __init__(self, farbe, alter):
        super().__init__(farbe, alter)

    def mach_geraeusch(self):
        super().mach_geraeusch()
        print("Der Hund bellt.")

# Der 'SchwarzeHund' ist eine reguläre Klasse und erbt alles von 'Hund' und 'Tier'.
# Da die Farbe durch den Namen der Klasse quasi schon vorgegeben ist,
# implemtieren wir hier einen neuen Konstruktor der nur noch das Alter akzeptiert.
# Beim Aufruf des Konstrukturs der Eltern-Klasse 'Hund' (super().__init()) wird 
# für die Farbe fest der Wert 'schwarz' übergeben und das Alter weitergeleitet.
class SchwarzerHund(Hund):
    def __init__(self, alter):
        super().__init__("schwarz", alter)


# - - - Test-Code / Demonstration  - - - - - - - - - - - - - - - - - - - - - - -

def main():
    # tier = Tier()     # wirft einen Fehler, da Instanzen von abstrakten Klassen nicht erlaubt sind
    hund = Hund("weiß", 7)
    schwarzer_hund = SchwarzerHund(2)

    hund.hallo()
    hund.mach_geraeusch()

    schwarzer_hund.hallo()
    schwarzer_hund.mach_geraeusch()

main()
