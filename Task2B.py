from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)
    tolerance = 0.8
    list_of_stations = stations_level_over_threshold(stations, tolerance)
    for i in list_of_stations:
        print(i[0], i[1])

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
