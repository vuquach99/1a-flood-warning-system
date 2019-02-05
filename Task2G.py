from floodsystem.stationdata import build_station_list, update_water_levels

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

    # Create list of unique towns
    town_list0 = []
    for station in stations:
        town_list0.append(station.town)
        town_list = list(set(town_list0))
        town_list.sort()
    
    # Create town lists
    severe_risk = []
    high_risk = []
    moderate_risk = []
    low_risk = []

    # Assess flood risks
    for station in stations:
        if (type(station.relative_water_level()) != type(None)):
            if float(station.relative_water_level()) >= 2:
                # Town is at severe risk
                severe_risk.append(station.town)
            elif 1.5 <= float(station.relative_water_level()) < 2:
                # Town is at high risk
                high_risk.append(station.town)
            elif 1.0 <= float(station.relative_water_level()) < 1.5:
                # Town is at moderate risk
                moderate_risk.append(station.town)
            elif float(station.relative_water_level()) < 1.0:
                # Town is at low risk
                low_risk.append(station.town)

    print ("Severe risk: {} station(s): {}".format(len(severe_risk), severe_risk))
    print ("High risk: {} station(s): {}".format(len(high_risk), high_risk))
    print ("Moderate risk: {} station(s): {}".format(len(moderate_risk), moderate_risk))
    print ("Low risk: {} station(s)".format(len(low_risk)))
        
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()  