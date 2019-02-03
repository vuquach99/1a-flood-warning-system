from datetime import datetime, timedelta

from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels

def test_plot():
    stations = build_station_list()

    for station in stations:
        if station.name == "Cam":
            station_cam = station
            break
    assert station_cam

    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1), datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4), datetime(2017, 1, 5)]
    level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    plot_water_levels(station_cam, t, level)

    