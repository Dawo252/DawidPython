import numpy as np
b = np.arange(9).reshape(3,3)
print(b)
for i in range(0,b.shape[0]):
        print(b[i], end=" ")
