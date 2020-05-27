import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


np.random.seed( 19680822 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
fig = plt.figure()

for i, n, rodzaj, kolor in ([121,20,'scatter','red'],[122,5,'plot','green']):
    ax = fig.add_subplot( i , projection = '3d' )
    xs = randrange(n, 10, 80)
    ys = randrange(n, 10, 80)
    zs = randrange(n, 0,0)
    if rodzaj=='scatter':
        ax.scatter(xs,ys,zs,c = kolor, marker = '8')
    elif rodzaj=='plot':
        ax.plot(xs,ys,zs,c = kolor, marker = '.')
plt.show()