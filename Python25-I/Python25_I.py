
# - - - Infos / Bücher / Links - - - - - - - - - - - - - - - - - - - - - - - - -

# Buch  Programmieren mit Python (westermann)  Kapitel 7.5  Abstrakte Klassen und Interfaces


# - - - Definitionen - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from abc import ABC, abstractmethod

# 'IUsbSpeicher' ist ein Interface (ein Spezialfall einer abstrakten Klasse), weil:
# - erbt von ABC
# - enthält ausschließlich abstrakte Methoden
class IUsbSpeicher(ABC):
    @abstractmethod
    def pruefe_speicher(self):
        pass

    @abstractmethod
    def pruefe_usb(self):
        pass

# 'Notebook' ist eine reguläre Klasse
# Da diese von 'IUsbSpeicher' erbt, muss 'Notebook' alle
# abstrakten Methoden implementieren.
class Notebook(IUsbSpeicher):
    def pruefe_speicher(self):
        return True             # besitzt Speicher, z.B. Festplatte
    
    def pruefe_usb(self):
        return True             # besitzt eine USB-Schnittstelle


class Digitalkamera(IUsbSpeicher):
    def pruefe_speicher(self):
        return True             # besitzt Speicher, z.B. SD-Card
    
    def pruefe_usb(self):
        return False            # aber keine USB-Schnittstelle
    

# - - - Test-Code / Demonstration  - - - - - - - - - - - - - - - - - - - - - - -

def main():
    print("Datenübertragung per USB wird vorbereitet...")
    print("Um Daten zu übertragen, bitte ein passendes Gerät verbinden!")

    geraet = Digitalkamera()

    # prüfe auf Speicher
    speicher_vorhanden = geraet.pruefe_speicher()
    if speicher_vorhanden:
        print("Speicher ist vorhanden")
    
    # prüfe auf USB-Verbindung
    usb_vorhanden = geraet.pruefe_usb()
    if usb_vorhanden:
        print("USB Vebrindung ist vorhanden")
    
    if speicher_vorhanden and usb_vorhanden:
        print("Daten werden übertragen...")
    else:
        print("Fehler: Daten können nicht übertragen werden!")

main()
