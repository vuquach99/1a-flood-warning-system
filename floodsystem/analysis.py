import matplotlib
import datetime
import numpy as np
from dateutil.tz import tzutc

def polyfit(dates, levels, p):
    """Task 2F: Returns a tuple of the polynomial object and any shift of the time axis"""
    # Convert dates to floats
    dates_float = matplotlib.dates.date2num(dates)

    # Find the time shift d0
    d0 = dates_float[0]
    dates_shifted = []
    for i in range(len(dates_float)):
        dates_shifted.append(dates_float[i] - dates_float[0])

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(dates_shifted, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    poly_tuples = (poly, d0)
    return poly_tuples

def warnings(stations):
    """Task 2G: Returns lists of risk-assessed towns"""
    # Create list of unique towns
    town_list0 = []
    for station in stations:
        town_list0.append(station.town)
        town_list = list(set(town_list0))
        town_list.sort()
    
    # Create town lists
    severe_risk = []
    high_risk = []
    moderate_risk = []
    low_risk = []

    # Assess flood risks
    for station in stations:
        if (type(station.relative_water_level()) != type(None)):
            if float(station.relative_water_level()) >= 2:
                # Town is at severe risk
                severe_risk.append(station.town)
            elif 1.5 <= float(station.relative_water_level()) < 2:
                # Town is at high risk
                high_risk.append(station.town)
            elif 1.0 <= float(station.relative_water_level()) < 1.5:
                # Town is at moderate risk
                moderate_risk.append(station.town)
            elif float(station.relative_water_level()) < 1.0:
                # Town is at low risk
                low_risk.append(station.town)

    # Append lists
    warnings = [severe_risk, high_risk, moderate_risk, low_risk]
    return warnings