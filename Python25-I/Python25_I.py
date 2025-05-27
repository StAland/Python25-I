def fakultaet(zahl):
    if zahl <= 1:
        return 1
    ergebnis = zahl * fakultaet(zahl-1)
    return ergebnis

def fibonacci(n):
    if n <= 2:
        return 1
    print(n)
    ergebnis = fibonacci(n-1) + fibonacci(n-2)
    return ergebnis

def main():
    ergebnis = fakultaet(500)
    print("Das Ergebnis ist: ", ergebnis)


main()
