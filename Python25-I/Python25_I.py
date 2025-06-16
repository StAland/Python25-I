def main():
    # haus1 = Haus(6, "gelb", 2)
    # print("Farbe: ", haus1.farbe)    

    # print("Stockwerke: ", haus1.get_stockwerke())
    # haus1.set_stockwerke("Hallo")
    # print("Stockwerke: ", haus1.get_stockwerke())
    # haus1.set_stockwerke(3)
    # print("Stockwerke: ", haus1.get_stockwerke())
    
    auto = Auto("Mazda 2", "gruen")
    print(auto.get_model(), " ", auto.get_farbe())
    
class Auto:
    def __init__(self, model, farbe):
        self.__model = model
        self.__farbe = farbe
    
    def get_model(self):
        return self.__model
    
    def get_farbe(self):
        return self.__farbe
    
    def set_farbe(self, value):
        self.__farbe = value

class Haus:
    def __init__(self, hoehe, farbe, stockwerke):
        self.hoehe = hoehe
        self.farbe = farbe
        if type(stockwerke) == int:
            self.__stockwerke = stockwerke
        else:
            self.__stockwerke = 1
            
    def get_stockwerke(self):
        return self.__stockwerke
    
    def set_stockwerke(self, value):
        if type(value) == int:
            self.__stockwerke = value

main()
