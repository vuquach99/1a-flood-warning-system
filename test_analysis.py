from floodsystem.analysis import polyfit 
import numpy as np

def test_analysis():
    x = np.linspace(0, 2, 10) 
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]
    
    assert type(x) == np.ndarray
    assert type(y) == list
    assert type(polyfit(x,y,4)) == type(None)