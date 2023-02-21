# Racing Cars Comparer

Projekt byl vytvořen v jazyce Python verze 3.8.5.

## Struktura projektu

Projekt se skládá ze souborů:

    main.py - Hlavní program aplikace
    car.py - Třída reprezentující automobil
    databaze_aut.py - Třída pro práci s databází automobilů
    zavod.py - Třída pro simulaci závodu mezi auty
    config.py - Konfigurační soubor s cestou k databázi automobilů
    README.md - Tento soubor

## Spuštění aplikace

Pro spuštění aplikace stačí spustit soubor main.py.

## Použití aplikace

Po spuštění aplikace se zobrazí hlavní menu:

`
1... Zobrazit Auta
2... Vytvoř Auto
3... Smazat Auto
4... Začít závod
n... Načíst auta
a... Uložit auta
z... Uložit závody

x... Konec
`

Volba se provede zadáním příslušného čísla a potvrzením klávesou Enter.

    Volba 1 zobrazí seznam všech automobilů v databázi
    Volba 2 umožní vytvoření nového automobilu a jeho uložení do databáze
    Volba 3 umožní smazání automobilu z databáze
    Volba 4 umožní spuštění simulace závodu mezi několika auty
    Volba n umožní načíst automobily ze souboru
    Volba a umožní uložení automobilů do souboru
    Volba z umožní uložení výsledků závodů do souboru
    Volba x ukončí aplikaci