#arytmetyczny.py

def suma(a1 = 1, r = 1, ile = 10):
    suma = 0
    if ile == 1:
        return a1
    else:
        while ile > 0:
            suma += a1
            a1 += r
            ile -= 1
        return suma

def iloczyn(a1 = 1, r = 1, ile = 10):
    iloczyn = 1
    if ile == 1:
        return a1
    else:
        while ile > 0:
            iloczyn *= a1
            a1 += r
            ile -= 1
        return iloczyn
