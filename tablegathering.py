"""Gathers all data to dataframes"""

import pandas as pd
from history import a
import numpy as np
from user_generator import UserRandomizer
from area_dict import gush_dan

pd.set_option('display.max_columns', 15)

user_generator = UserRandomizer(a)
passenger = user_generator.generate_passenger()
cities_per_area = pd.DataFrame.from_dict(gush_dan, orient='index').transpose()

stops = pd.read_csv(r'stops.csv')
stops.drop(['stop_id','stop_name','location_type', 'parent_station', 'zone_id'],axis='columns', inplace=True)
print(stops.head())