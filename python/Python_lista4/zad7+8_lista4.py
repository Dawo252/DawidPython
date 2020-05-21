class Robaczek:

    x = 0
    y = 0
    krok = 1

    def __init__ (self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += self.krok * ile_krokow
    
    def idz_w_dol(self, ile_krokow):
        self.y -= self.krok * ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x -= self.krok * ile_krokow

    def idz_w_prawo(self, ile_krokow):
        self.x += self.krok * ile_krokow
    
    def pokaz_gdzie_jestes(self):
        print("x=",self.x)
        print("y=",self.y)

    def __del__(self):
        del self.x
        del self.y
        del self.krok