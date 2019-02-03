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

    # Plot
    plot = plot_water_levels(risky_stations, 10)

    return plot

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()  