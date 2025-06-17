def main():
    haus = Mietshaus()
    wohnung1 = Wohnung(1000)
    wohnung2 = Wohnung(840)
    haus.add_wohnung(wohnung1)
    haus.add_wohnung(wohnung2)
    haus.add_wohnungspreis(1200)
    print(haus.get_Gesamtmiete())
    
class Mietshaus:
    
    def __init__(self):
        self.__wohnungsliste = []
        
    def add_wohnung(self, wohnung):
        if type(wohnung) == Wohnung:
            self.__wohnungsliste.append(wohnung)
            
    def add_wohnungspreis(self, preis):
        if type(preis) == int:
            self.__wohnungsliste.append(Wohnung(preis))
            
    def get_Gesamtmiete(self):
        summe = 0
        for wohnung in self.__wohnungsliste:
            summe += wohnung.get_miete()
        return summe
        
class Wohnung:
    
    def __init__(self, miete):
        self.__miete = miete
        
    def get_miete(self):
        return self.__miete

main()
