import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np


def calculates_trapezoid_area(b1, b2, h):
    return ((b1 + b2) * h) / 2


def num_expression(n):
    return n**2 + 5


def plot_graph(t1, a, b, num_trapz):
    # Plots function
    plt.plot(t1, num_expression(t1), 'b')

    # Plots trapezes
    ticks = float((b - a)) / num_trapz
    # Plots parallel lines
    for n in np.arange(a, b + 1, ticks):
        plt.plot([n, n], [0, num_expression(n)], 'r')

    # Plots slanted lines
    for n in np.arange(a, b, ticks):
        plt.plot([n, n + ticks], [num_expression(n), num_expression(n + ticks)], 'r')

    plt.grid(True)
    plt.show()


def main():
    # inputs
    a = 0
    b = 12
    num_trapz = 8

    t1 = np.arange(a, b, 0.01)

    # trapezoidal integration
    i = a
    area = 0
    while i < b:
        j = i + ((b - a) / num_trapz)
        area += calculates_trapezoid_area(
            num_expression(i),
            num_expression(j),
            (b - a) / num_trapz)
        i = j

    integral = quad(num_expression, a, b)
    integral = integral[0]
    relative_error = (integral - area) / integral

    print('Area using trapezoidal rule: {:0.3f}'.format(area))
    print('Area using integral: {:0.3f}'.format(integral))
    print('Relative error: {:0.3f}%'.format(relative_error * 100))

    plot_graph(t1, a, b, num_trapz)


if __name__ == '__main__':
    main()
