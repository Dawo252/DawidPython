def Parzyste(slowo):
    for index in range(0, len(slowo), 2):
        yield slowo[index]

cos = Parzyste("Sełwodń")
cos1 = iter(cos)
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))