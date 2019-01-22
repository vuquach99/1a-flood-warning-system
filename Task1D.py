from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()

rivers = rivers_with_station(stations)
print(rivers[:10])
print("\n")



dictionary = stations_by_river(stations)
riveraire = dictionary['River Aire']
riveraire.sort()
print(riveraire)
print("\n")

rivercam = dictionary['River Cam']
rivercam.sort()
print(rivercam)
print("\n")

thames = dictionary['Thames']
thames.sort()
print(thames)
print("\n")