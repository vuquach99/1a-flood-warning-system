# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from haversine import haversine


def stations_by_distance(stations, p):
    listforall = []
    for station in stations:
        listforall.append((station.name, haversine(station.coord, p)))
    sorted_by_key(listforall, 1)
    return listforall

def stations_within_radius(stations, centre, r):
    listofstations = []
    for station in stations:
        if (haversine(station.coord,centre) <= r):
            listofstations.append(station.name)
    return listofstations
