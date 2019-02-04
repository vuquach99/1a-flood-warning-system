import matplotlib
import datetime
import numpy as np
from dateutil.tz import tzutc

def polyfit(dates, levels, p):
    """Task 2F: Returns a tuple of the polynomial object and any shift of the time axis"""
    # Convert dates to floats
    dates_float = matplotlib.dates.date2num(dates)

    # Find the time shift d0
    d0 = dates_float[0]
    dates_shifted = []
    for i in range(len(dates_float)):
        dates_shifted.append(dates_float[i] - dates_float[0])

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(dates_shifted, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    poly_tuples = (poly, d0)
    return poly_tuples