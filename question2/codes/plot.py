import numpy as np
import matplotlib.pyplot as plt

# Load points from the data file
points = np.loadtxt("points.dat", delimiter=',')
x_circle1 = points[:101, 0]
y_circle1 = points[:101, 1]
x_circle2 = points[101:, 0]
y_circle2 = points[101:, 1]

# Circle 1 center and radius
center1 = ((x_circle1[0]+x_circle1[50])/2, (y_circle1[0]+y_circle1[50])/2)
radius1 = np.sqrt((x_circle1[0] - center1[0])**2 + (y_circle1[0] - center1[1])**2)
circle_eq1 = f'$(x - {center1[0]:.2f})^2 + (y - {center1[1]:.2f})^2 = {radius1**2:.2f}$'

# Circle 2 center and radius
center2 = ((x_circle2[0]+x_circle2[50])/2, (y_circle2[0]+y_circle2[50])/2)
radius2 = np.sqrt((x_circle2[0] - center2[0])**2 + (y_circle2[0] - center2[1])**2)
circle_eq2 = f'$(x - {center2[0]:.2f})^2 + (y - {center2[1]:.2f})^2 = {radius2**2:.2f}$'

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot the first circle in the first subplot
axes[0].plot(x_circle1, y_circle1, label='Circle 1', color='orange')
axes[0].fill(x_circle1, y_circle1, 'lightblue', alpha=0.5)
axes[0].scatter(*center1, color='red', label='Center 1')
axes[0].text(center1[0], center1[1], f'({center1[0]:.2f}, {center1[1]:.2f})', fontsize=10, ha='right')
axes[0].text(center1[0], center1[1] + radius1, circle_eq1, fontsize=12, ha='center', color='black')
axes[0].set_title("Circle 1")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].axis('equal')
axes[0].grid(True)
axes[0].legend(loc="upper right")

# Plot the second circle in the second subplot
axes[1].plot(x_circle2, y_circle2, label='Circle 2', color='green')
axes[1].fill(x_circle2, y_circle2, 'lightgreen', alpha=0.5)
axes[1].scatter(*center2, color='red', label='Center 2')
axes[1].text(center2[0], center2[1], f'({center2[0]:.2f}, {center2[1]:.2f})', fontsize=10, ha='right')
axes[1].text(center2[0], center2[1] + radius2, circle_eq2, fontsize=12, ha='center', color='black')
axes[1].set_title("Circle 2")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].axis('equal')
axes[1].grid(True)
axes[1].legend(loc="upper right")

# Adjust layout and show the plot
plt.tight_layout()
plt.savefig('/home/suraj5323/matgeoee11033/question2/figs/Figure_1.png')

