#Task12 - Vytvoříte generátor, který bude postupně vracet
# Albert - máme koncovku "bert".
# před tu koncovku budou dávány předpony "Al", "Ro", "Hu", "Nor", "Gil"

def GeneratorJmen(pred, konc):
    for pre_word in pred:
        yield pre_word + konc



    pass

predpony = ["Jir", "Sir", "Pil", "Bur", "Kul"]
koncovka = "ka"
for jmeno in GeneratorJmen(predpony, koncovka):
    print(f"Tvé jméno je {jmeno}") # Albert, Robert, Hubert, Norbert, Gilbert







