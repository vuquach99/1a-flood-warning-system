
def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

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
