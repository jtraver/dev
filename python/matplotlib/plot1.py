#!/usr/bin/python

# https://en.wikipedia.org/wiki/Matplotlib

import numpy
import matplotlib.pyplot as plt

from numpy.random import rand

a = rand(100)
b = rand(100)
plt.scatter(a, b)
plt.show()
