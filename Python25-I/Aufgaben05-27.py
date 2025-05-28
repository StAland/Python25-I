def zaehle():
    print("Aufgabe 1:")
    for zahl in range(1, 11, 1):
        print(zahl)

def gerade_zaehlen():
    print("Aufgabe 2:")
    for zahl in range(2, 21, 2):
        print(zahl)

def summe_bis(n):
    print("Aufgabe 3:")
    if n < 0:
        print("Bitte nur positive Zahlen benutzen")
        return
    ergebnis = 0
    for zahl in range(1, n+1):
        ergebnis += zahl
    print("Das Ergebnis ist: ", ergebnis)
    
def produkt_bis(n):
    print("Aufgabe 4:")
    if n < 1:
        print("Bitte nur positive Zahlen benutzen")
        return
    ergebnis = 1
    for zahl in range(2, n+1):
        ergebnis *= zahl
    print("Das Ergebnis ist: ", ergebnis)
    
def stern_quadrat(n):
    print("Aufgabe 5:")
    ausgabe = ""
    for durchlaufvariable in range(1, n+1):
        ausgabe += "*"
    for durchlaufvariable in range(1, n+1):
        print(ausgabe)
        
def dreieck(n):
    print("Aufgabe 6:")
    ausgabe = ""
    for i in range(1, n+1):
        ausgabe += "*"
        print(ausgabe)
        
def zaehle_zeichen(text, zeichen):
    print("Aufgabe 7:")
    anzahl = 0
    zeichen = zeichen.lower()
    for buchstabe in text.lower():
        if buchstabe == zeichen:
            anzahl += 1
    print("Das Zeichen ", zeichen, " kommt ", anzahl, "x vor")

def ist_prim(n):
    print("Aufgabe 8:")
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if (n % i == 0):
            return False
    return True

def ggt(a, b):
    groesser = 0
    kleiner = 0
    if a > b:
        groesser = a
        kleiner = b
    else:
        groesser = b
        kleiner = a
    while(groesser % kleiner != 0):
        rest = groesser % kleiner
        groesser = kleiner
        kleiner = rest
    print("Der ggt ist: ", kleiner)

def main():
    zaehle()
    print()
    gerade_zaehlen()
    print()
    summe_bis(6)
    print()
    produkt_bis(7)
    print()
    stern_quadrat(10)
    print()
    dreieck(7)
    print()
    zaehle_zeichen("Steffen", 's')
    print()
    print(ist_prim(13))
    print()
    ggt(225, 60)

main()