import numpy as np
import matplotlib.pyplot as plt

# Load the points from the values.dat file
points = np.loadtxt("values.dat", delimiter=',', max_rows=30)

# Extract x and y coordinates
x_values = points[:, 0]
y_values = points[:, 1]

# Define the endpoints of the line segment
A = np.array([-4, 6])  # Point A
B = np.array([-4, -6]) # Point B

# Create a figure
plt.figure()

# Plot the line segment from A to B
plt.plot([A[0], B[0]], [A[1], B[1]], label='Line Segment AB', color='blue')

# Plot the points from values.dat using plt.plot
plt.plot(x_values, y_values, 'ro', label='Points from values.dat')

# Annotate points A and B with their coordinates
plt.annotate(f'A ({A[0]}, {A[1]})', A, textcoords="offset points", xytext=(0,10), ha='center', color='blue')
plt.annotate(f'B ({B[0]}, {B[1]})', B, textcoords="offset points", xytext=(0,-15), ha='center', color='blue')

# Customize the plot
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Segment and Points from values.dat")
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.axis('equal')

# Show the plot
plt.show()

