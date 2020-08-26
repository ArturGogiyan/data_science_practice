from math import sin, exp
from matplotlib import pylab as plt
from scipy import linalg
import numpy as np


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


A = np.array([[1, 1, 1, 1], [1, 4, 4**2, 4**3], [1, 10, 100, 1000], [1, 15, 15**2, 15**3]])
b = np.array([f(1), f(4), f(10), f(15)])
A = linalg.solve(A, b)
file1 = open('result.txt', 'w')
file1.write(str(A[0]) + " " + str(A[1]) + " " + str(A[2]) + " " + str(A[3]))
file1.close()
plt.plot([1, 4, 10, 15], A)
t1 = np.arange(1, 15, 0.1)
t2 = [f(x) for x in t1]
plt.plot(t1, t2)
plt.show()
