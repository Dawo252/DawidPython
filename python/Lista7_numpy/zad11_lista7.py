import numpy as np

a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)
c = np.arange(12).reshape(2,6)

d = a.ravel()
e = b.ravel()
f = c.ravel()

print(d)
print(e)
print(f)
#identyczne