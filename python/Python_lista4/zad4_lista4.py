class NaZakupy:

    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0

    def __init__ (self, nazwa, ilosc, jednostka, cena):
        self.nazwa_produktu = nazwa
        self.ilosc = ilosc
        self.jednostka_miary = jednostka
        self.cena_jed = cena
    
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed)