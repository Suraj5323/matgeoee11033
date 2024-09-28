import matplotlib.pyplot as plt

# Read points from the file
points = []
with open('values.dat', 'r') as file:
    for _ in range(37):  # Read exactly 35 points
        line = file.readline().strip()
        if line:  # Check if the line is not empty
            x, y = map(float, line.split(','))
            points.append((x, y))

# Unzip the points into x and y coordinates
x_coords, y_coords = zip(*points)

# Plotting the points as a continuous line without markers
plt.figure(figsize=(10, 6))
plt.plot(x_coords, y_coords, color='blue', linestyle='-')  # Removed marker='o'
plt.title('2D Points from values.dat')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Label the endpoints
plt.text(x_coords[0], y_coords[0], f'({x_coords[0]}, {y_coords[0]})', fontsize=9, verticalalignment='top')
plt.text(x_coords[-1], y_coords[-1], f'({x_coords[-1]}, {y_coords[-1]})', fontsize=9, verticalalignment='bottom')

# Adjust axes limits to zoom out
plt.xlim(min(x_coords) - 3, max(x_coords) + 3)  # Increase the range by 2 units on both sides
plt.ylim(min(y_coords) - 3, max(y_coords) + 3)  # Increase the range by 2 units on both sides
plt.savefig('/home/suraj5323/matgeoee11033/question1/figs/Figure_1.png')

