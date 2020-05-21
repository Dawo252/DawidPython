with open("zad3_lista4.txt", "w+") as plik:
    plik.write("Kilka\n")
    plik.write("zapisanych linijek\n")
    plik.write("tekstu\n")
    plik.seek(0,0)
    for slowo in plik:
        print(slowo, end = "")
