import os
from databaze_aut import DatabazeAut
from zavod import Race
from config import path_to_cars, path_to_races

def main():
    databaze = DatabazeAut()
    zavody = []

    choice = "o"
    
    # Hlavní cyklus
    while choice != "x":
        os.system("clear") # Vyčištení konzole
        Menu() # Vypsání menu
        choice = input("> ") # Volba od uživatele

        # Zobrazení všech aut
        if(choice=="1"):
            databaze.Vypis_Auta()
        elif(choice=="2"):
            databaze.Vytvor_Auto()
        elif(choice=="3"):
            databaze.Vypis_Auta()
            index = input("Zadej číslo auta ke smazání: ")
            auto_ke_smazani = databaze.auta[index]
            databaze.Smaz_Auto(auto_ke_smazani)
        elif(choice=="4"):
            vzdalenost = input("Vzdálenost závodu (v m): ")
            
            databaze_pro_zavod = DatabazeAut()
            
            for index, auto in enumerate(databaze.auta):
                print(f"{index+1}. {auto}")
            cisla = input("Zadejte čísla aut pro závod oddělých mezerou [1 5 8 11]: ")
            indexy = [int(cislo) - 1 for cislo in cisla.split()]

            for i in indexy:
                databaze_pro_zavod.Pridej_Auto(databaze.auta[i])

            zavod = Race(vzdalenost,databaze_pro_zavod)
            zavod.Start_Race()
            zavody.append(zavod)
        elif(choice=="n"):
            soubory = []
            number=0
            for file in os.listdir(path_to_cars):
                if file.endswith(".txt"):
                    number+=1
                    print(f"{number}. {file}")
                    soubory.append(file)
            index = int(input("Zadejte číslo souboru pro načtení: "))
            nazev_souboru = soubory[index-1]
            databaze.Nacti_Auta(nazev_souboru)
        elif(choice=="a"):
            nazev_souboru = input("Zadej název souboru: ")
            databaze.Uloz_Auta(nazev_souboru+".txt")
        elif(choice=="z"):
            nazev_souboru = input("Zadej název souboru: ")
            with open(path_to_races+nazev_souboru+".txt","w",encoding="utf-8") as file:
                for z in zavody:
                    file.write(str(z))

        input()

def Menu():
    print("1... Zobrazit Auta")
    print("2... Vytvoř Auto")
    print("3... Smazat Auto")
    print("4... Začít závod")
    print("n... Načíst auta")
    print("a... Uložit auta")
    print("z... Uložit závody")
    print()
    print("x... Konec")

if __name__ == "__main__":
    main()