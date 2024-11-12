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

class Domestic_dog(Mammal):
    def __init__(self, breed: str, coat_color: str):
        self.breed = breed
        self.coat_color = coat_color





zvire1 = Animals("prase", 150, 6)

zvire1.look()
zvire1.breath()

