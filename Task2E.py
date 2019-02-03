import datetime

from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2E"""
    # Build list of stations
    stations = build_station_list()

    # Update water levels 
    update_water_levels(stations)

    # Build list of 5 riskiest stations
    risky_stations = stations_highest_rel_level(stations,5)

    print (risky_stations)
    name_list = []
    for i in range(len(risky_stations)):
        name_list.append(risky_stations[i][0])

    # Plot
    for station in stations:
        if station.name in name_list:
            dt = 10
            water_level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            date = water_level[0]
            levels = water_level[1]

    # Show plot 
            plot_water_levels(station, date, levels)
        
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()  