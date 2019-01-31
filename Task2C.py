from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    #Build a list of stations
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #Build a list of 10 stations with highest relative water levels
    list_of_stations = stations_highest_rel_level(stations, 10)
    #show each stations and relative water level
    for i in list_of_stations:
        print(i[0], i[1])


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()