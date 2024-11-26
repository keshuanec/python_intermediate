from time import time

class TimeMeasurment:
    def __init__(self):

    def __enter__(self):
        start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        print(end - start)



with TimeMeasurment() as t: #"Spouštím výpočet v čase 18:59.03"
    cislo = 1
    for i in range(10000000):
        cislo += i
    print(cislo) #49999995000001
#"Dokončeno v čase 18:59.05 - blok trval 3 sekundy