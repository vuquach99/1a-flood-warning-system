from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river

def test_stationsbydistance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    assert stations_by_distance(stations, p)[0] == ('Cambridge Jesus Lock', 0.840237595667494)

def test_stationwithinradius():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    assert stations_within_radius(stations,p,0) == []

def test_call_riverswithstation():
    stations = build_station_list()
    rivers_with_station(stations)

def test_call_stationsbyriver():
    stations = build_station_list()
    stations_by_river(stations)
