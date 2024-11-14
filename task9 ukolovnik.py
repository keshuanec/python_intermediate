# Task 9 - úkolovník
# Cílem úkolu je vytvořit poznámkový blok V poznámkovém bloku můžeme přidávat,
# odebírat nebo měnit řádky. Když spustíme program tak máme následující možnosti:
#
# Přidat poznámku (nakonec)
# Vypsat všechny poznámky
# Smazat poznámku (budeme vyzváni, jaký řádek smazat)
# Upravit poznámku (budeve vyzváni, jaký řádek a jak upravit)
# Uložit poznámky do souboru .csv (budeme vyzváni do jakého souboru)
# (Volitelně uložení i přes pickle)
# Načíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru)

def pridat(poznamka: str):
    """
    prida poznamku na konec ukolovniku
    :param poznamka: textovy retezec
    :return:
    """



seznam_operaci = "Přidat poznámku (nakonec) - \"pridat\"\nVypsat všechny poznámky - \"vypsat\"\nSmazat poznámku (budeme vyzváni, jaký řádek smazat - \"smazat\"\nUpravit poznámku (budeve vyzváni, jaký řádek a jak upravit) - \"upravit\"\nUložit poznámky do souboru .csv (budeme vyzváni do jakého souboru) - \"ulozit\"\nNačíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru) - \"nacist\"\nUkončit ukolovnik - \"ukoncit\""

operace = ""
while operace != "ukoncit":
    operace = input(
        f"{seznam_operaci}\n\nZapsáním klíčového slova uvedeného na konci řádku vyberte požadovanou operaci: ")

# soubor = input("zadejte nazev souboru s priponou .csv")
# with open(soubor)
# while input()
