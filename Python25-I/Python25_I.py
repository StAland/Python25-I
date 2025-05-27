def countdown(n):
    while n >= 0:
        print(n)
        n -= 1
        
def countup(n):
    for zahl in range(0, n+1, 1):   
        print(zahl)

def fac_iterativ(n):
    ergebnis = 1
    while n > 1:
        ergebnis *= n
        n -= 1
    return ergebnis

def array_ausgabe(n):
    for element in n:
        print(element)
        
def gib_Steffen_ein():
    eingabe = ""
    while eingabe != "Steffen":
        eingabe = input("Gib Steffen ein: ")

def main():
    #countdown(19)
    #print(fac_iterativ(10))
    #countup(15)
    # ar = [1, 6, 9, 10, "Hallo", 3.15]
    # ar[2] = 7
    # array_ausgabe(ar)
    gib_Steffen_ein()


main()
