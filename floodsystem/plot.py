import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """Task 2E: plots water level against time"""
    t = datetime.timedelta(days=dates)
    for station in station:

        
        level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

        #Assign variables
        range_high = station.typical_range[1]
        range_low = station.typical_range[0]

        # Plot
        plt.plot(t, level, label="$water level$")
        plt.plot(t, range_high, label="$typical low$")
        plt.plot(t, range_low, label="$typical low$")

        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title(station)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels

        return plt.show()