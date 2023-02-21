import math
import os
import time

class Race:
    def __init__(self, distance, database):
        self.distance = int(distance)
        self.database_of_cars = database
        self.winner = None
        self.ujeto = [0] * len(self.database_of_cars.auta)  # inicializace seznamu ujeto

    def Start_Race(self):
        seconds = 0
        while self.winner == None:
            seconds+=1
            os.system("clear")
            print(f"Čas {seconds} s")
            print(f"Vzdálenost {self.distance} m")
            for index, car in enumerate(self.database_of_cars.auta):  # oprava přístupu k autům
                car.jizda()
                self.ujeto[index] += car.rychlost  # oprava názvu atributu

                # přesun výpisu do samostatné metody
                self.Print_Race(car, index)

                print(f"Ujeto: {math.floor(self.ujeto[index])} m")
                print(f"Rychlost {car.rychlost} km/h")

                if self.ujeto[index] >= self.distance:
                    self.winner = car
            time.sleep(1)

        print(f"Vyhrál {self.winner}")

    def Print_Race(self, car, index):
        print(f"{index} {car.znacka} {car.model}")  # výpis značky a modelu auta

        max_points = 20
        print("[", end="")
        points = math.floor(max_points / (self.distance / self.ujeto[index]))  # oprava názvu atributu
        for i in range(max_points):  # oprava syntaxe
            if i < points:  # oprava podmínky
                print("-", end="")
            else:
                print(" ", end="")
        print("]")

    def __str__(self):
        auta_string = ""
        for auto in self.database_of_cars.auta:
            auta_string+=f"{auto}, "
        return f"Vítěz {self.winner}, Dráha {self.distance}, Všichni účastníci {auta_string}"
