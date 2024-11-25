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
import pickle




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

def ulozit_pickle(notes):
    with open('data.pickle', 'wb') as f:
        pickle.dump(notes, f)


def nacist():
    file_csv = input("zadejte nazev souboru k nacteni: ")
    with open(file_csv, 'r', encoding="utf-8", newline="") as work_file:
        reader = csv.reader(work_file)
        for line in reader:
            notes.extend(line)


def nacist_pickle():
    with open('data.pickle', 'rb') as f:
        notes = pickle.load(f)
    return notes


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
    elif operace == "ulozit_pickle":
        ulozit_pickle(notes)
    elif operace == "nacist_pickle":
        notes = nacist_pickle()
    elif operace == "ukoncit":
        print("Diky za pouziti. Program se ukoncuje.")
        break
    else:
        print("neznama operace")



# soubor = input("zadejte nazev souboru s priponou .csv")
# with open(soubor)
# while input()
