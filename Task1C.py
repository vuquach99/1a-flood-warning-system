from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
stations = build_station_list()

p = (52.2053, 0.1218)

listofstations = stations_within_radius(stations,p,10)
listofstations.sort()
print(listofstations)