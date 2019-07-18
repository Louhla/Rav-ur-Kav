"""Gathers all data to dataframes"""

import pandas as pd
from history import a
import numpy as np
from user_generator import UserRandomizer
from area_dict import gush_dan
from PricesGushDan import prices
import seaborn as sns
import matplotlib.pyplot as plt

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
stops['city'] = [' '.join(x.split(':')[2].split()[:-1]) for x in stops['stop_desc'].values]  # Extracted the cities here
# print(stops.head())

price_df = pd.DataFrame.from_dict(prices, orient='index')
# print(price_df.head())

translation_df = stops[stops['stop_code'].isin(passenger['Place'].values)].loc[:,['stop_code','city']]  # FOUND THE STOPS
passenger = pd.merge(passenger, translation_df, left_on=['Place'], right_on=['stop_code'])  # joined the city data to passenger df

areas = []

for row, city in enumerate(passenger['city'].values):
    area = cities_per_area.isin([city]).sum(axis=0)
    c = area[area == 1].index.values.astype(float)
    if len(c) == 0:
        areas.extend([1.])
        continue
    areas.extend(c)

passenger['region'] = areas

print(passenger)
