from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stationsleveloverthreshold():
    stations = build_station_list()
    update_water_levels(stations)
    assert stations_level_over_threshold(stations, 100000) == []
test_stationsleveloverthreshold()

def test_stationhighestrellevel():
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #Build a list of 10 stations with highest relative water levels
    assert stations_highest_rel_level(stations, 0) == [3]

test_stationhighestrellevel()