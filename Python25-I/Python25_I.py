
# - - - Infos / Bücher / Links - - - - - - - - - - - - - - - - - - - - - - - - -

# Buch  Programmieren mit Python (westermann)  Kapitel 7.4  Vererbung
# Buch  Python 3 Crashkurs (dpunkt.verlag)     Kapitel 9    Klassen / Vererbung
# Link  https://openbook.rheinwerk-verlag.de/python/21_002.html#u21.2


# - - - Definitionen - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class VerbrennerAuto:
    def __init__(self, hersteller, modell, farbe, kraftstoff):
        self.__hersteller = hersteller
        self.__modell = modell
        self.__farbe = farbe
        self.__kraftstoff = kraftstoff
    
    def set_farbe(self, value):
        if type(value) == str:
            self.__farbe = value
        else:
            print("Keine gültige Farbe!")
    
    def get_kraftstoff(self):
        return self.__kraftstoff

    def __str__(self):
        text = self.__hersteller + " " + self.__modell + " | "
        text += self.__farbe + " | "
        text += self.get_kraftstoff()
        return text

class ElektroAuto:
    def __init__(self, hersteller, modell, farbe, batterie_kWh):
        self.__hersteller = hersteller
        self.__modell = modell
        self.__farbe = farbe
        self.__batterie_kWh = batterie_kWh
    
    def set_farbe(self, value):
        if type(value) == str:
            self.__farbe = value
        else:
            print("Keine gültige Farbe!")
    
    def get_batterie_kWh(self):
        return self.__batterie_kWh

    def __str__(self):
        text = self.__hersteller + " " + self.__modell + " | "
        text += self.__farbe + " | "
        text += str(self.get_batterie_kWh()) + " kWh"
        return text


# - - - Test-Code / Demonstration  - - - - - - - - - - - - - - - - - - - - - - -

def main():
    verbrenner = VerbrennerAuto("Opel", "Corsa", "schwarz", "Benzin")
    elektro = ElektroAuto("Tesla", "Model S", "weiß", 85)

    print(verbrenner)
    print(elektro)

main()