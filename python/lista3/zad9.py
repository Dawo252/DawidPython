def iloczyn(* liczby):
    if len(liczby) == 0:
        return 0.0
    else:
        iloczyn = 1.0
        for i in liczby:
            iloczyn *= i
        return iloczyn
print(iloczyn())
print(iloczyn(1,2,3,4))