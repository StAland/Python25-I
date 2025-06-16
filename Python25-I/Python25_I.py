def main():
    haus1 = Haus(6, "gelb", 2)
    print("Farbe: ", haus1.farbe)
    haus2 = haus(6, "gelb", 2)
    print("Farbe: ", haus2["farbe"])

    

def haus(hoehe, farbe, stockwerke):
    return {"hoehe": hoehe, "farbe": farbe, "stockwerke": stockwerke}
    

class Haus:
    def __init__(self, hoehe, farbe, stockwerke):
        self.hoehe = hoehe
        self.farbe = farbe
        self.stockwerke = stockwerke

main()
