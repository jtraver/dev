#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from itertoolz import itertools # Standard mathematical coordinates can be mapped here

# 1. Define the center sphere
center = np.array([0, 0, 0])

# 2. Define the 12 kissing spheres (FCC / Cuboctahedron packing)
# Assuming sphere radius = 1, distance from center to outer centers = 2
directions = [ [1, -1, 0], [-1, 1, 0], [-1, -1, 0],
[1, 0, -1], [-1, 0, 1], [-1, 0, -1],
[0, 1, -1], [0, -1, 1], [0, -1, -1]
]
spheres = np.array(directions) * np.sqrt(2) / 2 * 2 # Normalized distance

# 3. Setup the 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot center
ax.scatter(center[0], center[1], center[2], color='white', s=500, edgecolors='black')

# Plot surrounding spheres with a color gradient matching your image
colors = plt.cm.rainbow(np.linspace(0, 1, 12))
for i, pos in enumerate(spheres):
    ax.scatter(pos[0], pos[1], pos[2], color=colors[i], s=500, alpha=0.6)

# 4. Add the Hill Tetrahedron (Vertices example)
# Hill tetrahedra have specific vertex ratios based on the space-filling properties
tetra_vertices = np.array([
    [1, np.sqrt(3), 0],
    [1, 1/np.sqrt(3), np.sqrt(8/3)]
]) * 2  # Scaled to encapsulate the spheres

# Plot tetrahedron edges
pairs = [(0,1), (1,2), (2,0), (0,3), (1,3), (2,3)]
for p in pairs:
    ax.plot3D(*zip(tetra_vertices[p[0]], tetra_vertices[p[1]]), color="gray", linestyle="--")

plt.show()

