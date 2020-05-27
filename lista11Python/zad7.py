import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed( 19680000 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
fig = plt.figure()

zs = 0
x = [0, 10, 25, 35, 45]
y = [10, 25, 25, 30, 35]

for  n, rodzaj, kolor, marker in ([20,'scatter','red', 'o' ],[5,'plot','green', 0]):
    ax = fig.gca( projection = '3d' )
    xs = randrange(n, 10, 80)
    ys = randrange(n, 10, 80)
    ax.scatter(xs, ys, zs, zdir = 'z', c = kolor, marker = marker)
    ax.plot(x, y, zs,c = kolor) #pojawiają się kreski (pewnie dlatego, że losowe punkty stworzyły się właśnie tam, ale nie wiem jak dokładnie określić ich wspólrzędne, żeby dać przez nie linię)
    ax.set_zlim(0,1)
    ax.set_xlabel( 'X' )
    ax.set_ylabel( 'Y' )
    ax.set_zlabel( 'Z' )
plt.show()