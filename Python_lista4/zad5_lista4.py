class Ciagi:
    a1=0
    r=1
    ilosc=0

    def wyswietl_dane(self):
        print(self.a1)
        print(self.r)
        print(self.ilosc)
    
    def pobierz_elementy(self, a1, r):
        self.a1 = a1
        self.r = r

    def pobierz_parametry(self, a1, r, ilosc):
        self.a1 = a1
        self.r = r
        self.ilosc = ilosc
    
    def policz_sume(self):
        return (((2*self.a1 + (self.ilosc - 1)*self.r))/2)*self.ilosc

    def policz_elementy(self):
        for i in range(self.ilosc):
            print(self.a1 + self.r * i, sep=" ")
