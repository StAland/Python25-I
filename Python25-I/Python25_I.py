import random

def wuerfeln():
    random.seed()
    zahl = random.randint(1, 6) # Int
    zahl = random.random() # float zwischen 0 und 1
    zahl = random.uniform(2.5, 9.1) # float zwischen a und b
    zahl = random.gauss(5, 2)
    return zahl

def messwerte_simulieren(anzahl, minwert, maxwert):
    messwerte = []
    random.seed()
    for i in range(0, anzahl):
        zahl = random.uniform(minwert, maxwert)
        messwerte.append(round(zahl, 2))
    return messwerte

def main():
    messwerte = messwerte_simulieren(75, -10, 40)
    print(messwerte)


main()
