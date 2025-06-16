def main():
    einkaufsliste = Einkaufsliste()
    einkaufsliste.artikel_hinzufuegen("Butter", 2)
    einkaufsliste.artikel_hinzufuegen("Honig", 1)
    einkaufsliste.artikel_entfernen("Butter")
    einkaufsliste.ausgabe()
    
class Einkaufsliste:
    
    def __init__(self, vorhandenesDictionary = {}):
        self.__liste = vorhandenesDictionary
        
    def artikel_hinzufuegen(self, artikel, anzahl):
        if artikel in self.__liste:
            self.__liste[artikel] += anzahl
        else:
            self.__liste[artikel] = anzahl
            
    def ausgabe(self):
        for artikel, anzahl in self.__liste.items():
            print(artikel, anzahl)
            
    def artikel_entfernen(self, artikel, anzahl = 1):
        if artikel in self.__liste:
            if self.__liste[artikel] > anzahl:
                self.__liste[artikel] -= anzahl
            else:
                del self.__liste[artikel]

main()
