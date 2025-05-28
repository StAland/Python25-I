


def main():
    text = "hallo"
    print(text.capitalize())
    print(text)
    text = "HaLLo"
    print(text.casefold()) #Seite 180 Fehler bei casefold der erste Buchstabe bleibt nicht gross
    print(text.center(10, "*")) #Wenn eine ungerade Anzahl an Fuellzeichen benutzt wird, wir hinten eins mehr verwendet
    print(text.count("L"))
    print(text.count("L",3,5))
    print(text.find("L"))
    print(text.find("l"))   #nicht gefunden gibt -1
    print(text.index("L"))
    #print(text.index("l"))  #nicht gefunden gibt einen Fehler
    print(text.rfind("L"))
    print(text.rindex("L"))
    print(text.isalpha())
    text2 = "Wasser02"
    print(text2.isalpha())
    text3 = "12.3423"
    print(text3.isdecimal())
    print(text.lower())
    print(text.upper())
    print(text.replace("L", "l"))
    
    

main()
