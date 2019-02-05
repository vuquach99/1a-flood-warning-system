from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stationsleveloverthreshold1():
    stations = build_station_list()
    update_water_levels(stations)
    assert stations_level_over_threshold(stations, 100000) == []

def test_stationsleveloverthreshold2():
    stations = build_station_list()
    update_water_levels(stations)
    assert stations_level_over_threshold(stations, 0) != []

def test_stationhighestrellevel1():
    stations = build_station_list()
    update_water_levels(stations)
    assert stations_highest_rel_level(stations, 0) == []

def test_stationhighestrellevel2():
    stations = build_station_list()
    update_water_levels(stations)
    assert stations_highest_rel_level(stations, 10) != []

test_stationsleveloverthreshold1()
test_stationhighestrellevel2()
test_stationsleveloverthreshold1()
test_stationsleveloverthreshold2()