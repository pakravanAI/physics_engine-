import matplotlib.pyplot as plt
import numpy as np

def plotpath(x_pos_list, y_pos_list):
    x = x_pos_list  # x position
    y = y_pos_list  # y position

    # Create the plot
    plt.figure(figsize=(8, 7))
    plt.plot(
        x, y,
        label='object path',
        color=(78/255, 191/255, 217/255),
        linewidth=1,
        marker='o',
        markersize=2
    )

    # Mark the starting position
    plt.scatter(
        x[0],
        y[0],
        color='green',
        s=80,
        zorder=5,
        label='starting position'
    )

    plt.annotate(
        'START',
        (x[0], y[0]),
        xytext=(10, 10),
        textcoords='offset points'
    )

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('position tracker')

    # Add grid and legend
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # Show the plot
    plt.show()
