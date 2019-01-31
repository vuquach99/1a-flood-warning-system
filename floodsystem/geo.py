# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    listforall = []
    for station in stations:
        listforall.append((station.name, haversine(station.coord, p)))
    sortedlist = sorted_by_key(listforall, 1)
    return sortedlist

def stations_within_radius(stations, centre, r):
    listofstations = []
    for station in stations:
        if (haversine(station.coord,centre) <= r):
            listofstations.append(station.name)
    return listofstations

def rivers_with_station(stations):
    listofrivers = []
    for station in stations:
        listofrivers.append(station.river)
        reallist = list(set(listofrivers))
        reallist.sort()
    return reallist

def stations_by_river(stations):
    dictionary = {}
    stationlist = []
    riverlist = []

    for river in rivers_with_station(stations):
        riverlist.append(river)
        stationsmalllist = []
        for station in stations:
            if (str(station.river) == str(river)):
                stationsmalllist.append(station.name)
        stationlist.append(stationsmalllist)
    keys = range(len(riverlist))
    for i in keys:
        dictionary[riverlist[i]] = stationlist[i]
    return dictionary
                