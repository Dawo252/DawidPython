class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(7,4)
p3 = Point(6,2)

print(p1.counter)
print(p2.counter)
print(p3.counter)
p1.update(7)
print(p1.counter)
p2.update(7)
print(p2.counter)
p3.update(2)
print(p3.counter)