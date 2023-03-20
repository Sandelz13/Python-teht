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
            print("Hissi saavutti kohteen kerroksen", self.kerros)

    def kerros_alas(self, kohde_kerros):
        while self.kerros > kohde_kerros and self.kerros > self.alin_kerros:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)
        if self.kerros == kohde_kerros:
            print("Hissi saavutti kohteen kerroksen", self.kerros)




class Talo:
    def __init__(self, alin_kerros, ylimmäinen_kerros, hissien_määrä):
        self.hissit = [Hissi(alin_kerros, ylimmäinen_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_nro, kohde_kerros):
        hissi = self.hissit[hissi_nro - 1]
        hissi.siirry_kerrokseen(kohde_kerros)


talo = Talo(1, 10, 2)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 3)