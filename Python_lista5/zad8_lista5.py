class Samogloski:

    samogloski = {"a", "e", "i", "o", "u", "y"}

    def __init__(self, tekst):
        if isinstance(tekst, str):
            self.tekst = tekst
        else:
            self.tekst = str(tekst)
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.tekst):
            raise StopIteration
        if self.tekst[self.index] in Samogloski.samogloski:
            return self.tekst[self.index]



cos=Samogloski("bbnahei")
cos1=iter(cos)
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))
cos2=Samogloski(454353454)
cos3=iter(cos2)
print(next(cos3))


