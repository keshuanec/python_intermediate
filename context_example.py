from datetime import datetime


class TimeMeasurment():
    def __init__(self):
        pass

    def __enter__(self):
        self.start = datetime.now()
        print(f"spoustim vypocet v {self.start.strftime('%H:%M:%S')}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.now()
        print(f"dokonceno v case {self.end.strftime('%H:%M:%S')}. Blok trval {self.end - self.start}")


with TimeMeasurment() as t:  # "Spouštím výpočet v čase 18:59.03"
    cislo = 1
    for i in range(10000000):
        cislo += i
    print(cislo)  # 49999995000001
# "Dokončeno v čase 18:59.05 - blok trval 3 sekundy
