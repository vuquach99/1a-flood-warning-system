from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
def run():
    #Build a list of stations
    stations = build_station_list()
    #Coordinate of Cambridge City Center
    p = (52.2053, 0.1218)
    #Show the 10 closest stations
    print(stations_by_distance(stations, p)[:10])
    print("\n")
    #Show the 10 farthest stations
    print(stations_by_distance(stations, p)[-10:])

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()