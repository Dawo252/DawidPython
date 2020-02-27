print("Hello world!")

tekst = "Hello world!"
tekst = 'Hello world!'
tekst = """Hello
 world!"""
tekst = 0
print(id(tekst))
print(type(tekst))
print(type("ala"))
print(type(5))
print(type(5.5))
print(type(True))
print(type(None))

print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
print(5 // 5) # dzielenie bez reszty
print(5 % 5)
print(5 ** 5) # potęgowanie

print("Ala" + "ma kota.")
print("Ala " + "ma " + str(5) + " lat")

liczba = int("100")
print(liczba)

print("Ala" * 10)

# Listy ---------------------------------------
lista = []
print(type(lista))
lista2 = [1, 2, 3]
print(lista2[0])
imie = "Magdalena"
print(imie[0])
lista2[0] = 5
# imie[0] = "K" błąd
print(imie.swapcase()) # tylko wyświetlenie
imie = imie.swapcase() # nadpisanie
print(imie)
"Ala".swapcase()
lista3 = [1, "Ala", 4.5, None, True, [1, 2]]
lista3[5][1]

macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
macierz[1][1] # wybiera 5 z macierzy u góry
nowa = lista2 + macierz

#słownik
slownik = {}
slownik['imie'] = 'Adam'
slownik[0] = 'Adam'
print(slownik)

slownik2 = {'imie': 'Adam', 0: 'Adam'}
print(slownik2.keys())
print(slownik2.values())

def pow():
    pass

from math import *
import math as m

print(m.pow(e,10))

