# Code by GVV Sharma
# July 22, 2024
# released under GNU GPL
# Line 

import sys                                          # for path to external scripts
sys.path.insert(0, '/home/suraj5323/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports (commented out since we're not using these functions anymore)
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Given points from output.dat file
data = np.genfromtxt('output.dat', delimiter=' ', names=True)
x = data['X']
y = data['Y']
A = np.array(([x[0], y[0]])).reshape(-1, 1)
B = np.array(([x[1], y[1]])).reshape(-1, 1)
C = np.array(([x[2], y[2]])).reshape(-1, 1)

# Plotting line segments without using line_gen
plt.plot([A[0, 0], B[0, 0]], [A[1, 0], B[1, 0]], label='$distance(AB)$')
plt.plot([B[0, 0], C[0, 0]], [B[1, 0], C[1, 0]], label='$distance(BC)$')

# Labeling the coordinates
quad_coords = np.hstack([A, B, C])
plt.scatter(quad_coords[0, :], quad_coords[1, :], c=np.arange(1, 4))

vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({quad_coords[0, i]:.2f}, {quad_coords[1, i]:.2f})',
                 (quad_coords[0, i], quad_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(-10, -5),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

# use set_position for axes
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Axis labels, grid, and title
plt.xlabel('$X$-Axis')
plt.ylabel('$Y$-Axis')
plt.grid()  # minor
plt.axis('equal')
plt.title('Showing that A, B, C are collinear', loc='right', pad=15)
plt.legend(loc='best')
plt.show()

