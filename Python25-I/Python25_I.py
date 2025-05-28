
def main():
    notenliste = {"Dirk": 3.7, "John": 2.0, "Michael": 1.3}
    notenliste["Michael"] = 1.7
    notenliste["Jessica"] = 1.0
    notenliste2 = {"Steffen": 4.0, "John": 1.7}
    notenliste.update(notenliste2)  
    notenliste3 = notenliste.copy()
    noteSteffen = notenliste.pop("Steffen")
    del notenliste["Dirk"]
    notenliste.clear()
    print(notenliste3)
    print(notenliste)

main()
