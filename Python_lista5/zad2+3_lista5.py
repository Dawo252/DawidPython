class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik



class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    
    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

    def __add__(self, other):
        cala_dlugosc = self.x + other.x
        return 'Kwadrat o boku {}'.format(cala_dlugosc)

    def __ge__(self, other):
        if (self.x >= other.x):
           return True
        return False

    def __gt__(self, other):
        if (self.x > other.x):
           return True
        return False
    
    def __le__(self, other):
        if (self.x <= other.x):
            return True
        return False

    def __lt__(self, other):
        if (self.x < other.x):
            return True
        return False


figura = Kwadrat(3)
figura2 = Kwadrat(4)
print(figura + figura2)

if(figura < figura2):
    print("Pierwszy kwadrat jest wiekszy")
else:
    print("Drugi kwadrat jest wiekszy")

