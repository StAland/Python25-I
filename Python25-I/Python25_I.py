
# - - - Infos / Bücher / Links - - - - - - - - - - - - - - - - - - - - - - - - -

# Buch  Programmieren mit Python (westermann)  Kapitel 7.6  Mehrfachvererbung
# Link  https://openbook.rheinwerk-verlag.de/python/21_002.html#u21.2.5
# Link  https://openbook.rheinwerk-verlag.de/oop/oop_kapitel_05_004.htm#mj4744a80ac0ff520167d0124d73dba2b2


# - - - Definitionen - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Tier:
    pass

class Hund(Tier):
    pass

class SchwarzenHund(Hund):      # KEINE Mehrfachvererbung !!!
    pass


class Basis_1:
    def methode(self):
        print("methode von Basis_1")

class Basis_2:
    def methode(self):
        print("methode von Basis_2")

class AbgeleiteteKlasse(Basis_2, Basis_1):      # 'echte' Mehrverfachvererbung
    def methode(self):
        Basis_1.methode(self)

class C:
    def __init__(self):
        self.__basis_1 = Basis_1()      # keine Mehrverfachvererbung
        self.__basis_2 = Basis_2()      # alternative Implementierung als Komposition
    
    def methode(self):
        self.__basis_1.methode()

    def methode_2(self):
        self.__basis_2.methode()


# - - - Test-Code / Demonstration  - - - - - - - - - - - - - - - - - - - - - - -

def main():
    abgeleitete_klasse = AbgeleiteteKlasse()
    abgeleitete_klasse.methode()

    c = C()
    c.methode()
    c.methode_2()

main()
