'''
Created on Nov 15, 2016

@author: songjiguo
'''

import numpy as np
import matplotlib as p
import pdb
from pandas import *

data = pandas.read_csv("data/weather_year.csv")
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

print (data.mean_temp.head())


print (data.mean_temp.std())
