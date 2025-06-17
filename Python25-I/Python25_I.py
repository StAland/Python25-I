def main():
    hund = Haustier("Doggie", "Hund")
    hund.set_name(12)
    print(hund.get_name())
    hund.set_name("Chani")
    print(hund.get_name())
    
class Haustier:
    def __init__(self, name, art):
        self.__name = name
        self.__art = art
        
    def get_name(self):
        return self.__name
    
    def get_art(self):
        return self.__art
    
    def set_name(self, neuer_name):
        if type(neuer_name) == str and neuer_name != "":
            self.__name = neuer_name

main()
