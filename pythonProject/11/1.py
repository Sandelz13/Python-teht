class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print("Julkaisun nimi:", self.nimi)


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumaara)


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Päätoimittaja:", self.paatoimittaja)

if __name__ == "__main__":
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    print()
    hytti.tulosta_tiedot()
