from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    #Build a list of stations
    stations = build_station_list()
    #Cam City Center coordinates
    p = (52.2053, 0.1218)
    #Use the station within radius function to find stations within 10km
    listofstations = stations_within_radius(stations,p,10)
    #Sort the stations
    listofstations.sort()
    #Display the stations
    print(listofstations)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()