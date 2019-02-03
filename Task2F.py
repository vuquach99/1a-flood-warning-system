import numpy as np
import matplotlib.pyplot as plt

from floodsystem.plot import plot_water_level_with_fit

def run():
    """Requirements for Task 2F"""
    # Create set of 10 data points on interval (0, 2)
    x = np.linspace(0, 2, 10)
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x, y, 4)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))

    # Display plot
    plt.show()

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()  