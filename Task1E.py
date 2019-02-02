from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E"""
    #Build a list of stations
    stations = build_station_list(True)
    #Build river list
    list_of_rivers = rivers_by_station_number(stations, 9)
    print (list_of_rivers)
    

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()  
