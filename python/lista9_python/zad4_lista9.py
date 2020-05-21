import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
target = iris.target

plt.scatter(iris.data[:,0], iris.data[:,1], c=iris.target)

plt.show()