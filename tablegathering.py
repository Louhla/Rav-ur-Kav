"""Gathers all data to dataframes"""

import pandas as pd
from history import a
import numpy as np
from user_generator import UserRandomizer
from area_dict import gush_dan
from PricesGushDan import prices
import matplotlib.pyplot as plt
import six


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

passenger['city'] = passenger['city'].str.replace('ירושלים', 'אשדוד')
passenger_counts = passenger.groupby('city').count()
passenger_counts['Price Paid'] = passenger_counts['Place'] * 5.9
print(passenger_counts)

areas = []

for row, city in enumerate(passenger['city'].values):
    area = cities_per_area.isin([city]).sum(axis=0)
    c = area[area == 1].index.values.astype(float)
    if len(c) == 0:
        areas.extend([1.])
        continue
    areas.extend(c)

passenger['region'] = areas

# sns.set()
# sns.barplot(passenger['region'].value_counts().transpose())
# plt.show()

print(passenger['region'].value_counts())


def render_mpl_table(data, filename,col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors)])
    fig = ax.get_figure()
    fig.savefig(filename)
    pass

render_mpl_table(passenger, 'random_passengertable.png', header_columns=0, col_width=2.0)
