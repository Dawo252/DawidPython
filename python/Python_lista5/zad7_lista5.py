class Parzyste:

    def __init__(self, data):
        self.data = data
        self.index = -2
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index + 2
        return self.data[self.index]



cos = Parzyste("Sełwodń")
cos1 = iter(cos)
print(next(cos1))
print(next(cos1))
print(next(cos1))
print(next(cos1))
