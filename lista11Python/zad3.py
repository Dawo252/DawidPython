import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig =  plt.figure()

colormaps=['binary', 'gray', 'bone', 'pink','spring',
            'summer', 'autumn', 'winter', 'cool',
            'Wistia', 'hot', 'copper']

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt( x**2 + y**2 )
z = np.sin(r)

for i in range(321,326,1):
    ax = fig.add_subplot(i, projection = '3d')
    surf = ax.plot_surface(x, y, z, cmap = colormaps[i-321] , linewidth = 0, antialiased = False)
    ax.set_zlim(- 1.01 , 1.01 )
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink = 0.5, aspect = 5)

plt.show()