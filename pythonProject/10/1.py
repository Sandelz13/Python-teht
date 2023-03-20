class Hissi:
    def __init__(self, alin_kerros, ylimmäinen_kerros):
        self.ajossa = False
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimmäinen_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if not self.ajossa:
            self.ajossa = True
            if kohde_kerros > self.kerros:
                self.kerros_ylös(kohde_kerros)
            elif kohde_kerros < self.kerros:
                self.kerros_alas(kohde_kerros)
            self.ajossa = False

    def kerros_ylös(self, kohde_kerros):
        while self.kerros < kohde_kerros and self.kerros < self.ylin_kerros:
            self.kerros += 1
            print("Hissi on kerroksessa", self.kerros)
        if self.kerros == kohde_kerros:
            print("Hissi saavutti kerroksen", self.kerros)

    def kerros_alas(self, kohde_kerros):
        while self.kerros > kohde_kerros and self.kerros > self.alin_kerros:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)
        if self.kerros == kohde_kerros:
            print("Hissi saavutti kerroksen", self.kerros)


hissi = Hissi(1, 10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)