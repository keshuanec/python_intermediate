#Task 13 - zároveň sčítáme a násobíme

#cílem bude paralerně počítat:
# součet čísel 1,2,3,4,...1000000
# násobení čísel 1, 2, 3,4, .... 100


#Vložit třídu ThreadWithReturnValue

# definovat funkce pro sčítání a násobení

# inicializovat třídu ThreadWithReturnValue pro každou úlohu

# pustit  .start()

# počkat na výsledek .join()
#
# vysledek_scitani =
# vysledek_nasobeni =

# vyprintovat výsledky

import threading

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args =(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result

def scitani():
    vysledek_scitani = 0
    for i in range(1000000):
        vysledek_scitani += i
    return vysledek_scitani

def nasobeni():
    vysledek_nasobeni = 1
    for i in range(1,100):
        vysledek_nasobeni *= i
    return vysledek_nasobeni


if __name__ == "__main__":
    t1 = ThreadWithReturnValue(target=scitani)
    t2 = ThreadWithReturnValue(target=nasobeni)

    t1.start()
    t2.start()

    print(t1.join())
    print(t2.join())





#
# vysledek_scitani =
# vysledek_nasobeni =

