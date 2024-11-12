class Animals:
    def __init__(self, Weight: int, Age: int):
        self.Weight = Weight
        self.Age = Age

    def look(self):
        print(f"to je ale hezke {self}")

    def breath(self):
        print(f"zhluboka se nadechni pane {self}")


prase = Animals(96,5)

prase.look()
prase.breath()
