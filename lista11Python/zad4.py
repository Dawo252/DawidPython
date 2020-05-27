import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure( figsize =( 8 , 3 ))
for x in range (151, 156, 1):
    ax1 = fig.add_subplot( 151 , projection = '3d' )
    ax2 = fig.add_subplot( 152 , projection = '3d' )
    ax3 = fig.add_subplot( 153 , projection = '3d' )
    ax4 = fig.add_subplot( 154 , projection = '3d' )
    ax5 = fig.add_subplot( 155 , projection = '3d' )

    _x = np.arange( 4 )
    _y = np.arange( 5 )
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax1.bar3d(x, y, bottom, width, depth, top, shade = True)
    ax1.set_title('Wykres zacieniony')
    ax2.bar3d(x, y, bottom, width, depth, top, shade = False)
    ax2.set_title('Wykres nie zacieniony')
    ax3.bar3d(x, y, bottom, width, depth, top, shade = True , alpha = 0.2, color = 'purple')
    ax3.set_title('Czesciowo przezroczysty')
    ax4.bar3d(x, y, bottom, width, depth, top, shade = True, color = 'g', zsort='min') ## znalazłem zsort w dokumentacji ale nie wiem co robi
    ax4.set_title('Wykres z krawiedziami')
    ax5.bar3d(x, y, bottom, width, depth, top, shade = False, color = 'cyan', edgecolor=['r','g','blue'])
    ax5.set_title('Wykres z krawiedziami')

plt.show()