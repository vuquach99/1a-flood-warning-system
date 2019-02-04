import datetime
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def run():
    """Requirements for Task 2F"""
    # Build list of stations
    stations = build_station_list()

    # Update water levels 
    update_water_levels(stations)

    # Build list of 5 riskiest stations
    risky_stations = stations_highest_rel_level(stations,5)
    name_list = []
    for i in range(len(risky_stations)):
        name_list.append(risky_stations[i][0])
    
    # Collect water level data
    for station in stations:
        if station.name in name_list:
            dt = 2
            water_level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            date = water_level[0]
            levels = water_level[1]
            plot_water_level_with_fit(station, date, levels, 4)
            print ("Station name: {}".format(station.name))
            print (polyfit(date, levels, 4))
            print ("*****")
            
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()  