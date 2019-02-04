import matplotlib
import datetime
import numpy as np

def polyfit(dates, levels, p):
    """Task 2F: Returns a tuple of the polynomial object and any shift of the time axis"""

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    print (poly)