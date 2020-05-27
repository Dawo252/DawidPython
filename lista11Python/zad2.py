import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100

# Dla każdego zbioru styli i zakresów wygeneruj n losowych punktów
# zdefiniowane przez x z [23, 32], y in [0, 100], z z [zlow, zhigh].
for kolor, market, zlow, zhigh in [( 'r' , 'o' , - 50 , - 40 ), ( 'b' , '^' , - 40 , - 30 ), ('g', '.', -30, -20), ('purple', 'v', -20, -10), ('brown', 'X', -10, 0)]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =kolor, marker =marker)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()