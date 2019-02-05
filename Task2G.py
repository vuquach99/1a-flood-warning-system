from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import warnings

def run():
    """Requirements for Task 2G"""
    # Build list of stations with towns associated
    stations0 = build_station_list()
    stations = []
    for station in stations0:
        if (type(station.town) is not type(None)):
            stations.append(station)

    # Update water levels 
    update_water_levels(stations)

    # Create town lists
    w = warnings (stations)
    severe_risk = w[0]
    high_risk = w[1]
    moderate_risk = w[2]
    low_risk = w[3]

    # Print lists
    print ("Severe risk: {} station(s): {}".format(len(severe_risk), severe_risk))
    print ("High risk: {} station(s): {}".format(len(high_risk), high_risk))
    print ("Moderate risk: {} station(s): {}".format(len(moderate_risk), moderate_risk))
    print ("Low risk: {} station(s)".format(len(low_risk)))
        
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()  