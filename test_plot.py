import datetime
import numpy as np
from dateutil.tz import tzutc

from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

def test_plot_2e():
    stations = build_station_list()

    for station in stations:
        if station.name == "Cam":
            station_cam = station
            break
    assert station_cam

    t = [datetime.datetime(2016, 12, 30), datetime.datetime(2016, 12, 31), datetime.datetime(2017, 1, 1), datetime.datetime(2017, 1, 2), datetime.datetime(2017, 1, 3), datetime.datetime(2017, 1, 4), datetime.datetime(2017, 1, 5)]
    level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    plot_water_levels(station_cam, t, level)


def test_plot_2f():
    stations = build_station_list()
    
    for station in stations:
        if station.name == "Cam":
            station_cam = station
            break
    assert station_cam

    x = [datetime.datetime(2019, 2, 3, 0, 15, tzinfo=tzutc()), datetime.datetime(2019, 2, 3, 0, 0, tzinfo=tzutc()), datetime.datetime(2019, 2, 2, 23, 45, tzinfo=tzutc()), datetime.datetime(2019, 2, 2, 23, 30, tzinfo=tzutc()), datetime.datetime(2019, 2, 2, 23, 15, tzinfo=tzutc())]
    level = [0.2, 0.7, 0.95, 0.92, 1.02]

    plot_water_level_with_fit(station, x, level, 5)