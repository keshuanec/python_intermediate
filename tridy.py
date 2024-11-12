class Animals:
    def __init__(self, species: str, weight: int, age: int):
        self.species = species
        self.weight = weight
        self.age = age

    def look(self):
        print(f"to je ale hezke {self.species}")

    def breath(self):
        print(f"zhluboka se nadechni pane {self.species}")

class Mammal(Animals):
    def run(self):
        print(f"utikej {self.species}")

class Bird(Animals):
    def fly(self):
        print(f"koukej odletet {self.species}")

class Fish(Animals):
    def swim(self):
        print(f"odplav {self.species}")
    def print_info(self):
        print(f"tato ryba plave")

class Domestic_dog(Mammal):
    def __init__(self,species, weight, age, breed: str, coat_color: str):
        super().__init__(species, weight, age)
        self.breed = breed
        self.coat_color = coat_color
    def print_info(self):
        print(f"teento pejsek ma rasu {self.breed}")


class Pso_Ryba(Fish, Domestic_dog):
    def __str__(self):
        return f"to je divne zvire. Jmenuje se {self.species}, vazi {self.weight}, je mu {self.age} let a je rasy {self.breed}. A navic je {self.coat_color}"

podivnost = Pso_Ryba("divnej",56, 22, "kokr", "ruzovy")


podivnost.print_info()
print(podivnost)

#
#
#
#
# zvire1 = Animals("prase", 150, 6)
#
# zvire1.look()
# zvire1.breath()
#
# zvire5 = Domestic_dog("pes",15, 5, "vlcak", "modra")
#
