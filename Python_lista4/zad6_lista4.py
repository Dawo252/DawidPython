class Slowa:

    slowo1 = "kajak"
    slowo2 = "bambosze"


    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    
    def sprawdz_czy_palindrom(self):
        for i in range (len(self.slowo1)):
            if self.slowo1[i] != self.slowo1[len(self.slowo1)-i-1]:
                print("nie jest")
            elif self.slowo1[i] == self.slowo1[len(self.slowo1)-i-1]:
                print("jest")
        for i in range (len(self.slowo2)):
            if self.slowo2[i] != self.slowo2[len(self.slowo2)-i-1]:
                print("nie jest")
            elif self.slowo2[i] == self.slowo2[len(self.slowo2)-i-1]:
                print("jest")
    
    def sprawdz_czy_metagramy(self):
        sa = False
        if len(self.slowo1) == len(self.slowo2):
            rozne = 0
            for i in range (len(self.slowo1)):
                if self.slowo1[i]!=self.slowo2[i]:
                    rozne = rozne + 1
            if rozne == 1:
                sa = True
        if sa == True:
            print("są")
        else:
            print("nie są")

    def sprawdz_czy_anagramy(self):
        sa=True
        if len(self.slowo1)==len(self.slowo2):
            slowo = self.slowo2
            for znak in self.slowo1:
                if znak in slowo:
                    i = slowo.index(znak)
                    slowo = slowo[:i]+slowo[i+1:]
                else:
                    sa=False
        else:
            sa=False
        if sa == True:
            print("są")
        else:
            print("nie są")
        

    def wyswietl_wyrazy(self):
        print(self.slowo1)
        print(self.slowo2)



slowa=Slowa("aaaaaa", "aaaaaa")
slowa.sprawdz_czy_metagramy()
slowa.wyswietl_wyrazy()
slowa.sprawdz_czy_anagramy()