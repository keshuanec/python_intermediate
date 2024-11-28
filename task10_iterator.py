#Task 11 - udělat iterátor, kterému řekneme kolik chceme čísel, např. 5.
#Iterátor bude postupně vracet mocniny těchto čísel. Tzn pro číslo 5, iterátor vrátí 1, 4, 9, 16, 25


class IteratorMocnin:
    def __init__(self,n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.generated_numbers += 1
        if self.generated_numbers <= self.n:
            self.number += 1
            return (self.number - 1) * (self.number - 1)

        else:
            raise StopIteration



























mocniny = IteratorMocnin(5)
for mocnina in mocniny:
    print(mocnina)

#1
#4
#9
#16
#25