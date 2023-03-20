class Hissi:
    def __init__(self, alin_kerros, ylimmainen_kerros):
        self.ajossa = False
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimmainen_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if not self.ajossa:
            self.ajossa = True
            if kohde_kerros > self.kerros:
                self.kerros_ylos(kohde_kerros)
            elif kohde_kerros < self.kerros:
                self.kerros_alas(kohde_kerros)
            self.ajossa = False

    def kerros_ylos(self, kohde_kerros):
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
    def __init__(self, alin_kerros, ylimmainen_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylimmainen_kerros))

    def aja_hissia(self, hissin_nro, kohde_kerros):
        hissi = self.hissit[hissin_nro-1]
        hissi.siirry_kerrokseen(kohde_kerros)

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit menevät takaisin alas pohjakerrokseen!")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)



talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 7)
talo.aja_hissia(3, 3)


talo.palohalytys()
print("Kaikki hissit takaisin ykköskerroksessa")
