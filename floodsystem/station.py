# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
<<<<<<< HEAD

    def typical_range_consistent(self, waterrange):
        """Checks the typical high/low range data"""
        self.waterrange = self.typical_range[1] - self.typical_range[0]
        if type(waterrange) != type(None):
            if (self.waterrange == None) or self.waterrange < 0:
                return False #data is inconsistent 
            else:
                return True #data is consistent
        else: 
            return False 
        
=======
    
    def relative_water_level(self):
        if ((type(self.latest_level) == type(None)) or (type(self.typical_range) == type(None))):
            return None
        else:
            rwl = (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
            return rwl
>>>>>>> 24950f60668a8ea6b2a4b3ec2113e57f77beb383
