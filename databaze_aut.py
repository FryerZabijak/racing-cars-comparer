from car import Auto
from config import path_to_cars

class DatabazeAut:
    auta = []

    def Vypis_Auta(self, cislovani=True):
        number = 0
        for auto in self.auta:
            number+=1
            if cislovani:
                print(f"{number}. {auto}")
            else: 
                print(f"{auto}")

    def Vytvor_Auto(self):
        znacka = input("Zadej Značku: ")
        model = input("Zadej Model: ")
        barva = input("Zadej Barvu: ")
        zrychleni = input("Zadej Zrychlení: ")
        rychlost_max = input("Zadej Maximální Rychlost: ")
        new_car = Auto(znacka,model,barva,zrychleni,rychlost_max)
        self.auta.append(new_car)

    def Pridej_Auto(self, Auto):
        self.auta.append(Auto)

    def Nacti_Auta(self, soubor):
        cars = []
        with open(path_to_cars+soubor, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:  # přeskočení prvního řádku s názvy sloupců
                values = line.strip().split(",")
                brand, model, color, acceleration, max_speed = values
                car = Auto(brand,model,color,acceleration,max_speed)
                cars.append(car)
        self.auta = cars

    def Uloz_Auta(self, nazevSouboru):
        heading = "Značka | Model | Barva | Zrychlení | Rychlost Max\n"
        with open(path_to_cars+nazevSouboru, "w", encoding="utf-8") as file:
            file.write(heading)
            for c in self.auta:
                file.write(f"{c.znacka}, {c.model}, {c.barva}, {c.zrychleni}, {c.rychlost_max}\n")

    def Smaz_Auto(self, Auto):
        self.auta.remove(Auto)