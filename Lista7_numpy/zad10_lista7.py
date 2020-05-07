import numpy as np
b = np.arange(81).reshape(9,9)
print(b)

a = b.ravel()
print(a)

#nie działa transpozycja
##print(c) 

d = b.reshape(3,27)#bo 3*27 = 81
print(d)

e = b.reshape(27,3)#bo 3*27 = 81
print(e)

