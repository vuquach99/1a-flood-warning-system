from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""
    stations = build_station_list()

    badstations = inconsistent_typical_range_stations(stations)
    return print (badstations)
    

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()  