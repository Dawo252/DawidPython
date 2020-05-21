class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

cos = Wspak("Dawid")
cos1 = iter(cos)
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))

cos2 = Wspak([1,8,12,7,8])
cos3 = iter(cos2)
print(next(cos3))
print(next(cos3))
print(next(cos3))
print(next(cos3))
print(next(cos3))

#cos4 = Wspak({2,9,13,8,131})
#cos5 = iter(cos4)
#print(next(cos5))
#print(next(cos5))
#print(next(cos5))
#print(next(cos5))
#print(next(cos5))