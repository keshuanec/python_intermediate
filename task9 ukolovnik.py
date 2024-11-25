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
import csv



notes = []



def pridat():
    """
    prida poznamku na konec ukolovniku
    :param poznamka: promena pod kterou je poznamkovnik ulozen v pameti
    :return:
    """
    return f"{input("vloz poznamku: ")}"

def vypsat(notes):
    """
    vypise obsah aktualniho pracovniho prostoru
    :param notes:
    :return:
    """
    for line in notes:
        print(line)

def smazat(notes):
    """
    smaze zloveny radek z pracovniho prostoru
    :param notes:
    :return:
    """
    vypsat(notes)
    del_row = int(input("ktery radek chcete smazat? Zadejte jeho poradi: ")) - 1
    notes.pop(del_row)
    return notes

def upravit(notes):
    """
    nahradi zvoleny radek jinym textem
    :param notes:
    :return:
    """
    vypsat(notes)
    edit_row = int(input("ktery radek chcete upravit? Zadejte jeho poradi: ")) - 1
    notes[edit_row] = input(f"zadejte novy text do radku {edit_row + 1}: ")
    return notes

def ulozit(notes):
    file = input("zadejte nazev souboru csv: ")
    if ".csv" in file:
        file_csv = file
    else:
        file_csv = file + ".csv"
    with open(file_csv, 'a', encoding="utf-8", newline="") as work_file:
        writer = csv.writer(work_file)
        for line in notes:
            writer.writerow([line])

def nacist():
    file_csv = input("zadejte nazev souboru k nacteni: ")
    with open(file_csv, 'r', encoding="utf-8", newline="") as work_file:
        for line in work_file:
            notes.append(line)
        print(notes)




seznam_operaci = "seznam moznych operaci: pridat, vypsat, smazat, upravit, ulozit, nacist"   #"Přidat poznámku (nakonec) - \"pridat\"\nVypsat všechny poznámky - \"vypsat\"\nSmazat poznámku (budeme vyzváni, jaký řádek smazat - \"smazat\"\nUpravit poznámku (budeve vyzváni, jaký řádek a jak upravit) - \"upravit\"\nUložit poznámky do souboru .csv (budeme vyzváni do jakého souboru) - \"ulozit\"\nNačíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru) - \"nacist\"\nUkončit ukolovnik - \"ukoncit\""

operace = ""
while operace != "ukoncit":
    operace = input(f"{seznam_operaci}\n\nZapsáním klíčového slova uvedeneho v seznamu vyse vyberte požadovanou operaci: ")
    if operace == "pridat":
        notes.append(pridat())
    elif operace == "vypsat":
        vypsat(notes)
    elif operace == "smazat":
        notes = smazat(notes)
    elif operace == "upravit":
        notes = upravit(notes)
    elif operace == "ulozit":
        ulozit(notes)
    elif operace == "nacist":
        nacist()
    else:
        print("neznama operace")



# soubor = input("zadejte nazev souboru s priponou .csv")
# with open(soubor)
# while input()
