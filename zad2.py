from random import seed, random

macierz = [[random() for y in range(1+4*x, 5+4*x)] for x in range (4)]

lista = [macierz[x][x] for x in range(4)]
print(lista)