"""modul for saving cars series"""  # doc modul


class CarFactoryIterator():
    def __iter__(self):
        pass

    def __next__(self):
        if not self.serii:
            raise StopIteration
        return self.serii.pop(0)

    def __init__(self, serii):
        self.serii = serii


class CarFactory():
    """                 
    this is a class for storing class series, lot
    """  # doc clasa
    serii = []
    loturi = []

    def __init__(self, serie_start: int, numar_bucati: int):
        """
        
        :param serie_start: this is start series
        :param numar_bucati: this is numbers of cars produced
        """  # doc metoda
        self.serie_start = serie_start
        self.numar_bucati = numar_bucati
        self.__calcul_serii()
        self.__calcul_loturi()

    def __calcul_serii(self):
        self.serii = list(range(self.serie_start, self.serie_start + self.numar_bucati))

    def __calcul_loturi(self):
        lot_start = self.serie_start // 20
        lot_stop = (self.serie_start + self.numar_bucati) // 20

        lot_start += 1 if self.serie_start % 20 else 0
        # sauuuuuu
        # if not self.serie_start % 20:
        #     lot_start + 0
        # else:
        #     lot_start + 1

        lot_stop += 1 if (self.serie_start + self.numar_bucati) % 20 else 0
        # sauuuuu
        # if not (self.serie_start + self.numar_bucati) % 20:
        #     lot_stop + 0
        # else:
        #     lot_stop + 1

        self.loturi = list(range(lot_start, lot_stop + 1))

    def serii_stanga(self) -> list:
        """

        :return: series number for cars with wheel left
        """
        lista_serii_stanga = []
        for serie in self.serii:
            if serie % 2:
                lista_serii_stanga.append(serie)
        return lista_serii_stanga

    def serii_dreapta(self) -> list:
        """

        :return: series number for cars with right wheel
        """
        lista_serii_dreapta = []
        for serie in self.serii:
            if not serie % 2:
                lista_serii_dreapta.append(serie)
        return lista_serii_dreapta

    def __iter__(self) -> CarFactoryIterator:
        return CarFactoryIterator(self.serii)


car_factory = CarFactory(314, 90)
print(car_factory.serii)
print(len(car_factory.serii))
print(car_factory.loturi)
print(car_factory.serii_stanga())
print(car_factory.serii_dreapta())

with open("tema6.txt", mode='x') as file:
    for car in car_factory:
        print(car)
        file.write(str(car) + '\n')

# for car in car_factory:
#     print(car)
