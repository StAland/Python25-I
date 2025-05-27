def fakultaet(zahl):
    if zahl <= 1:
        return 1
    ergebnis = zahl * fakultaet(zahl-1)
    return ergebnis


def main():
    ergebnis = fakultaet(6)
    print("Das Ergebnis ist: ", ergebnis)


main()
