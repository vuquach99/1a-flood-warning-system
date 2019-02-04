import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import datetime
from dateutil.tz import tzutc

def plot_water_levels(station, dates, levels):
    """Task 2E: Plots water level against time"""   
    #Assign variables
    range_high = [station.typical_range[1]]*len(dates)
    range_low = [station.typical_range[0]]*len(dates)

    # Plot
    plt.plot(dates, levels, label="Water Level")
    plt.plot(dates, range_high, label="Typical High")
    plt.plot(dates, range_low, label="Typical Low")

    # Add axis labels, add legend, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    return plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Task 2F: Plots the water level data and the best-fit polynomial"""
    # Convert dates to floats
    dates_float = matplotlib.dates.date2num(dates)

    # Create a shifted time list
    dates_shifted = []
    for i in range(len(dates_float)):
        dates_shifted.append(dates_float[i] - dates_float[0])

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(dates_shifted, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(dates_shifted, levels, '.', label='Data Points')

    # Plot polynomial fit and typical range low/high at 30 points along interval
    # (note that polynomial is evaluated using the date shift)
    x = np.linspace(dates_shifted[0], dates_shifted[-1], 30)
    range_high = [station.typical_range[1]]*len(x)
    range_low = [station.typical_range[0]]*len(x)
    
    plt.plot(x, poly(x - x[0]), label="Polynomial Fit")
    plt.plot(x, range_high, label="Typical High")
    plt.plot(x, range_low, label="Typical Low")

    # Add axis labels, add legend, rotate date labels and add plot title
    plt.xlabel('Dates from {}'.format(dates[-1]))
    plt.ylabel('Water Level (m)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    return plt.show()