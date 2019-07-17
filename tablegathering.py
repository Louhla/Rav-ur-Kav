"""Gathers all data to dataframes"""

import pandas as pd
from history import a
import numpy as np
from user_generator import UserRandomizer
from area_dict import gush_dan
from PricesGushDan import prices
import re

pattern_re = re.compile(r'/עיר:\s(.+)\sרציף:/')
pd.set_option('display.max_columns', 15)

user_generator = UserRandomizer(a)
passenger = user_generator.generate_passenger()
passenger.drop(['Debit_amount'], axis=1, inplace=True)
passenger.dropna(inplace=True)
# print(passenger)

cities_per_area = pd.DataFrame.from_dict(gush_dan, orient='index').transpose()
# print(cities_per_area)

stops = pd.read_csv(r'stops.csv')
stops.drop(['stop_id', 'stop_name', 'location_type', 'parent_station', 'zone_id'], axis='columns', inplace=True)
stops.drop(13755, inplace=True)
stops['city'] = [' '.join(x.split(':')[2].split()[:-1]) for x in stops['stop_desc'].values]  # TODO: Extracted the cities here
# print(stops['stop_desc'].values[0])
# print(pattern_re.match(stops['stop_desc'].values[0]))
# print(stops.head())

price_df = pd.DataFrame.from_dict(prices, orient='index')
# print(price_df.head())


# print(stops[stops['stop_code'].isin(passenger['Place'].values)])  # TODO: FOUND THE STOPS

