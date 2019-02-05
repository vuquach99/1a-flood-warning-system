from floodsystem.analysis import polyfit, warnings
from floodsystem.stationdata import build_station_list
import numpy as np

def test_analysis_2f():
    x = np.linspace(0, 2, 10) 
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]
    
    assert type(x) == np.ndarray
    assert type(y) == list

def test_analysis_2g():
    y = build_station_list()
    stations = []
    for station in y:
        if (type(station.town) is not type(None)):
            stations.append(station)
    x = warnings(stations)
    assert type(x) == list
    for i in range(len(x)):
        assert type(x[i]) == list
