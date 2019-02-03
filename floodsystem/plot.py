import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """Task 2E: plots water level against time"""
    
    #Assign variables
    range_high = [station.typical_range[1]]*len(dates)
    range_low = [station.typical_range[0]]*len(dates)

    # Plot
    plt.plot(dates, levels, label="Water Level")
    plt.plot(dates, range_high, label="Typical High")
    plt.plot(dates, range_low, label="Typical Low")

    # Add axis labels, add axis legend, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    return plt.show()