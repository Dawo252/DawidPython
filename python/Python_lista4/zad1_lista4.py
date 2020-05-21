from random import random

lista = [round(1000*random())for x in range(14) if x % 4 == 0]
print(lista)

plik = open("zad2_lista4.txt", "w")

plik.writelines(str(lista))

plik.close()