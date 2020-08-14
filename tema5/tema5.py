

class Triunghi():
    def __init__(self, a=60, b=60, c=60):
        self.a = a
        self.b = b
        self.c = c

    def modifica_unghi(self, unghi, grade):
        if grade not in range(0, 180):
            raise AttributeError
        else:
            if unghi is self.a:
                self.a = grade
                self.b = (180 - grade) / 2
                self.c = (180 - grade) / 2
            if unghi is self.b:
                self.b = grade
                self.c = (180 - grade) / 2
                self.a = (180 - grade) / 2
            if unghi is self.c:
                self.c = grade
                self.a = (180 - grade) / 2
                self.b = (180 - grade) / 2


triunghi = Triunghi()
print(triunghi.a, triunghi.b, triunghi.c)
triunghi.modifica_unghi(triunghi.b, 120)
print(triunghi.a, triunghi.b, triunghi.c)
