def Fibonacci(liczba):
    a = 0
    suma = 1
    while suma < liczba:
        yield suma
        c = a + suma
        a = suma
        suma = c

gen = Fibonacci(40)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

