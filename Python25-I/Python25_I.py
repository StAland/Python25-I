def main():
    notenliste = [1.7, 2.3, 1.0, 3.0]
    print(notenschnitt(notenliste))

def notenschnitt(notenliste):
    summe = sum(notenliste)
    anzahl = len(notenliste)
    
    return summe / anzahl

main()
