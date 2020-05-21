def monotonicznosc(a, b):
    if a>0:
        return "rosnąca"
    elif a<0:
        return "malejąca"
    else:
        return "stała"

print(monotonicznosc(4,5))