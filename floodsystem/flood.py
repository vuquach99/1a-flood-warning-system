
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    stations_list = []
    for station in stations:
        if (type(station.relative_water_level()) != type(None)):
            if (float(station.relative_water_level()) > tol):
                stations_list.append((station.name, station.relative_water_level()))
    return sorted_by_key(stations_list, 1, True)


def stations_highest_rel_level(stations, N):
    stations_list = []
    for station in stations:
        if (type(station.relative_water_level()) != type(None)):
            stations_list.append((station.name, station.relative_water_level()))
    sortedlist = sorted_by_key(stations_list, 1, True)
    return sortedlist[0:N]
