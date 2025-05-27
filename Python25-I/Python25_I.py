def umfang(radius):
    PI = 3.14
    return 2*PI*radius


def addieren(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    print(zahl1, "+", zahl2,"=",ergebnis)
    return ergebnis

def main():
    addieren(13, 12)
    addieren(1.2, 12)
    ergebnis = umfang(10)
    print("Der Umfang betraegt: ", ergebnis)



main()
