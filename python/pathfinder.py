import matplotlib.pyplot as plt

plot__ = None

posX = [0,1,2,3,4,5,6,7,8,9,10]
posY = [3,5,7,3,5,7,8,4,2,4,11]

def make_plot():
    global plot__

    figure, plot__ = plt.subplots(figsize=(8, 8))
    plot__.set_aspect('equal', adjustable='box')


def plotpath(x_pos_list, y_pos_list):
    x = x_pos_list
    y = y_pos_list

    plot__.plot(
        x, y,
        label='object path',
        color=(78/255, 191/255, 217/255),
        linewidth=1,
        marker='o',
        markersize=2
    )

    plot__.scatter(
        x[0],
        y[0],
        color='green',
        s=80,
        zorder=5,
        label='starting position'
    )

    plot__.annotate(
        'START',
        (x[0], y[0]),
        xytext=(10, 10),
        textcoords='offset points'
    )

    plot__.set_xlabel('X-axis')
    plot__.set_ylabel('Y-axis')
    plot__.set_title('position tracker')

    plot__.grid(True, linestyle='--', alpha=0.6)
    plot__.legend()

def __show__():

    plt.show()

