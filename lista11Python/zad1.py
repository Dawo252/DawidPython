from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca( projection = '3d')

t = np.linspace( 0, 2*np.pi, 100)
z = t
x = np.sin(z)
y = np.cos(z) *2
ax.plot(x, y, z, label = 'zad1')
ax.legend()
plt.show()