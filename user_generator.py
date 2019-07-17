import pandas as pd
from history import a
import numpy as np

# all_trips = []

# for user in a:
#     trips = []
#     for j in user['events']:
#         all_trips.append([j["timestamp"], j["transport_mean"], j["place"], j["line_number"], j["debit_amount"]])
#     # first_lvl.append(trips)
#
# df = pd.DataFrame(all_trips, columns=['Timestamp', 'Mode', 'Place', 'Line', 'Debit_amount'])
# df['Timestamp'] = pd.to_datetime(df['Timestamp'], format=('%Y-%m-%d')).dt.date
# print(df)


class UserRandomizer:
    def __init__(self, jsonlist):
        self.df = UserRandomizer.organize_df(jsonlist)
        self.get_num_available()

    @staticmethod
    def organize_df(listdict):
        all_trips = []
        for user in listdict:
            for j in user['events']:
                all_trips.append([j["timestamp"], j["transport_mean"], j["place"], j["line_number"], j["debit_amount"]])
        df = pd.DataFrame(all_trips, columns=['Timestamp', 'Mode', 'Place', 'Line', 'Debit_amount'])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format=('%Y-%m-%d')).dt.date
        return df

    def get_num_available(self):
        self.num_available_trips = len(self.df)
        pass

    def generate_passenger(self):
        num_of_trips = np.random.randint(1, self.num_available_trips)
        trips = np.random.choice(np.array(list(range(self.num_available_trips))), replace=False, size=num_of_trips)
        return self.df.iloc[trips, :].copy()

# b = UserRandomizer(a)
# print(b.generate_passenger())