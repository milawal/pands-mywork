# Plottask
# This program generates the required histogram and function plot in a visually appealing manner
# Author: Michael Lawal
# Reference: Matplotlib for plotting, NumPy for numerical calculations.

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean=5 and std=2
mean = 5
std_dev = 2
num_samples = 1000
data = np.random.normal(mean, std_dev, num_samples)

# Define the function h(x) = x^3
def h(x):
    return x ** 3

# Generate x values for the function plot (range 0 to 10)
x_values = np.linspace(0, 10, 100)
y_values = h(x_values)

# Create the plot
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.6, color='b', edgecolor='black', label='Histogram (Normal Distribution)')
plt.plot(x_values, y_values, 'r-', linewidth=2, label='$h(x) = x^3$')

# Labels and title
plt.xlabel('X-axis')
plt.ylabel('Frequency / Function Value')
plt.title('Histogram and Function Plot')
plt.legend()
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('plot.png')

# Show the plot
plt.show()
 