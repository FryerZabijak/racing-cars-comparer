class Auto:
    def __init__(self, znacka, model, barva, zrychleni, rychlost_max):
        self.znacka = znacka
        self.model = model
        self.barva = barva
        self.rychlost = 0
        self.zrychleni = zrychleni
        self.rychlost_max = int(rychlost_max)
        self.ujeta_vzdalenost = 0
        
    def zrychlit(self):
        # Přidání rychlosti k rychlosti
        self.rychlost += int(self.zrychleni)

        # Pokud rychlost překročila maximální, nastaví se na maximální
        if(self.rychlost > self.rychlost_max):
            self.rychlost = self.rychlost_max

    def pripocitej_vzdalenost(self):
        self.ujeta_vzdalenost+=self.rychlost

    def jizda(self):
        self.zrychlit()
        self.pripocitej_vzdalenost()
            
    def zobrazit_info(self):
        print("Značka:", self.znacka)
        print("Model:", self.model)
        print("Barva:", self.barva)
        print("Rychlost:", self.rychlost)

    def __str__(self):
        return f"Auto {self.znacka} {self.model} - barva {self.barva}"