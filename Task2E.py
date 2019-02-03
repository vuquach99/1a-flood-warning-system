import datetime

from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 2E"""
    # Build list of stations
    stations = build_station_list()

    # Build list of 5 riskiest stations
    risky_stations = stations_highest_rel_level(stations,5)

    # Create Variables

    dates = fetch_measure_levels[0]
    levels = fetch_measure_levels[1]

    # Plot
    for i in range(len(risky_stations)):
        plot = plot_water_levels(risky_stations[i], dates, levels)
    
    return plot

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()  