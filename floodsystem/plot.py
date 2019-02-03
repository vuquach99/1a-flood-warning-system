import matplotlib.pyplot as plt
import numpy as np

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
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(dates, levels, 4)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    
    # Plot original data points
    plt.plot(dates, levels, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the date shift)
    dates1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(dates1, poly(dates1 - dates[0]))

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    return plt.show()