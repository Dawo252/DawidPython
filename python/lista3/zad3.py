slownik = {"mieso": "kg", "jajka": "szt", "masło": "kostki"}
print(slownik)
lista = [key for key in slownik if slownik[key] == "szt"]
print(lista)