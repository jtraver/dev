#!/usr/bin/python

# https://matplotlib.org/api/animation_api.html

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)

def init():
    ax.set_xlim(0, 2*np.pi)
    # ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    #ax.set_xlim(-10, 10)
    #ax.set_ylim(-10, 10)
    return ln,

def update(frame):
    print "frame = %s " % str(frame)
    xdata.append(frame)
    sin1 = np.sin(frame)
    print "sin1 = %s " % str(sin1)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

#ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                    init_func=init, blit=True)
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=False)
#ani = FuncAnimation(fig, update, frames=np.linspace(0, 6, 2),
#                    init_func=init, blit=False)
# print "ani = %s" % str(ani)
plt.show()
