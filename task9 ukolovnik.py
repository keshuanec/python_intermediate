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

notes = ""

def pridat(notes:str):
    """
    prida poznamku na konec ukolovniku
    :param poznamka: promena pod kterou je poznamkovnik ulozen v pameti
    :return:
    """
    notes += f"{input("vloz poznamku: ")}\n"
    return notes

def vypsat(notes):
    """
    vypise obsah aktualniho pracovniho prostoru
    :param notes:
    :return:
    """
    print(f"\naktualni obsah poznamkovniku je:\n-------------------------------------------------------------------------------------------\n\n{notes} \n-------------------------------------------------------------------------------------------\n")

def smazat(notes):
    """
    smaze zloveny radek z pracovniho prostoru
    :param notes:
    :return:
    """
    print(notes)
    del_row = int(input("ktery radek chcete smazat? Zadejte jeho poradi: ")) - 1
    lines_list = notes.splitlines()
    lines_list.pop(del_row)
    notes = ""
    for line in lines_list:
        notes += f"{line}\n"
    return notes

def upravit(notes):
    """
    nahradi zvoleny radek jinym textem
    :param notes:
    :return:
    """
    print(notes)
    edit_row = int(input("ktery radek chcete upravit? Zadejte jeho poradi: ")) - 1
    lines_list = notes.splitlines()
    lines_list[edit_row] = input(f"zadejte novy text do radku {edit_row + 1}: ")
    notes = ""
    for line in lines_list:
        notes += f"{line}\n"
    return notes

def ulozit(notes):
    file = input("zadejte nazev souboru csv: ")
    with open():



seznam_operaci = "Přidat poznámku (nakonec) - \"pridat\"\nVypsat všechny poznámky - \"vypsat\"\nSmazat poznámku (budeme vyzváni, jaký řádek smazat - \"smazat\"\nUpravit poznámku (budeve vyzváni, jaký řádek a jak upravit) - \"upravit\"\nUložit poznámky do souboru .csv (budeme vyzváni do jakého souboru) - \"ulozit\"\nNačíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru) - \"nacist\"\nUkončit ukolovnik - \"ukoncit\""

operace = ""
while operace != "ukoncit":
    operace = input(f"{seznam_operaci}\n\nZapsáním klíčového slova uvedeného na konci řádku vyberte požadovanou operaci: ")
    if operace == "pridat":
        notes = pridat(notes)
    elif operace == "vypsat":
        vypsat(notes)
    elif operace == "smazat":
        notes = smazat(notes)
    elif operace == "upravit":
        notes = upravit(notes)
    elif operace == "ulozit":
        ulozit(notes)



# soubor = input("zadejte nazev souboru s priponou .csv")
# with open(soubor)
# while input()
