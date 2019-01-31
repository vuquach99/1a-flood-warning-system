from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    #Build a list of stations
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #set tolerance level
    tolerance = 0.8
    #Make a list of all stations with relative water levels above tolerance
    list_of_stations = stations_level_over_threshold(stations, tolerance)
    #show each station name and relative water level
    for i in list_of_stations:
        print(i[0], i[1])

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
