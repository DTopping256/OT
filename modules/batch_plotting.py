# Graph the accuraty of a model when multiple batches are run with different starting values
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from mpl_toolkits.mplot3d import Axes3D as plot3d

def get_sd(z, expected_z, sd):
    if sd == 0.0:
        return 0.0
    else:
        return abs(expected_z-z)/sd

def plot_2d_batch_accuracy(dependant_variable_name, independant_variable_name, expected_dependant_value, data):
    data_length = len(data)
    xs = np.array([i["x"] for i in data])
    ys = np.array([i["y"] for i in data])

    # MatPlotLib

    # How independant var affects dependant var (using other starting vars)
    plt.title('{} with respect to {}'.format(dependant_variable_name.capitalize(), independant_variable_name))
    plt.scatter(xs, ys, c='b', marker="d", label="Results")
    if (expected_dependant_value is not False):
        plt.plot([xs[0], xs[-1]], [expected_dependant_value, expected_dependant_value], "-g", label='Target ({})'.format(expected_dependant_value))
    plt.legend(framealpha=0.4)
    plt.xlabel(independant_variable_name)
    plt.ylabel(dependant_variable_name)
    plt.show()

    if (expected_dependant_value is not False):
        # Calc SD of dependant data
        sd = stat.stdev(ys, expected_dependant_value)
        sds = np.array([get_sd(y, expected_dependant_value, sd) for y in ys])

        # How independant var affects the standard deviation from target (of dependant var)
        plt.title('Standard deviation with {}'.format(independant_variable_name))
        plt.scatter(xs, sds, c='r', marker="d", label='SD (1 SD = {})'.format(round(sd, 2)))
        plt.legend(framealpha=0.4)
        plt.xlabel(independant_variable_name)
        plt.ylabel('Standard deviation from target ({})'.format(expected_dependant_value))
        plt.show()


def plot_3d_batch_accuracy(x_name, y_name, z_name, expected_z_value, data):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #plt.title('How {} & {} affect {}'.format(str.capitalize(x_name), y_name, z_name))

    xs = np.array([d["x"] for d in data])
    ys = np.array([d["y"] for d in data])
    zs = np.array([d["z"] for d in data])

    # Plot a 3d scatter of the data
    ax.scatter(xs, ys, zs, c="b", marker="x")

    # Customize the z axis.
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.set_zlabel(z_name)
    plt.show()

    if (expected_z_value is not False):
        # Calc SD of dependant data
        sd = stat.stdev(zs, expected_z_value)
        sds = np.array([get_sd(z, expected_z_value, sd) for z in zs])

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Plot a 3d scatter of the data with SD
        ax.scatter(xs, ys, sds, c="r", marker="x")

        # Customize the z axis.
        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        ax.set_zlabel('Standard deviation from target ({})'.format(expected_z_value))
        plt.show()
