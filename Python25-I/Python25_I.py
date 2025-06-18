
# - - - Infos / Bücher / Links - - - - - - - - - - - - - - - - - - - - - - - - -

# Buch  Programmieren mit Python (westermann)  Kapitel 7.6  Mehrfachvererbung
# Link  https://openbook.rheinwerk-verlag.de/python/21_002.html#u21.2.5
# Link  https://openbook.rheinwerk-verlag.de/oop/oop_kapitel_05_004.htm#mj4744a80ac0ff520167d0124d73dba2b2
# Link  https://de.wikipedia.org/wiki/Mehrfachvererbung

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

class IName(ABC):
    @abstractmethod
    def get_name(self):
        pass

class IHdmi(ABC):
    @abstractmethod
    def pruefe_hdmi(self):
        pass

# 'Notebook' ist eine reguläre Klasse
# Da diese von 'IUsbSpeicher' erbt, muss 'Notebook' alle
# abstrakten Methoden implementieren.
class Notebook(IUsbSpeicher, IName, IHdmi):
    def pruefe_speicher(self):
        return True             # besitzt Speicher, z.B. Festplatte
    
    def pruefe_usb(self):
        return True             # besitzt eine USB-Schnittstelle
    
    def get_name(self):
        return "Notebook"
    
    def pruefe_hdmi(self):
        return True


class Digitalkamera(IUsbSpeicher, IName):
    def pruefe_speicher(self):
        return True             # besitzt Speicher, z.B. SD-Card
    
    def pruefe_usb(self):
        return False            # aber keine USB-Schnittstelle
    
    def get_name(self):
        return "Digitalkamera"
    

# - - - Test-Code / Demonstration  - - - - - - - - - - - - - - - - - - - - - - -

def main():
    print("Datenübertragung per USB wird vorbereitet...")
    print("Um Daten zu übertragen, bitte ein passendes Gerät verbinden!")

    geraet = Notebook()

    # identifiziere Gerät
    print("Folgendes Gerät wurde angeschlossen", geraet.get_name())

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
