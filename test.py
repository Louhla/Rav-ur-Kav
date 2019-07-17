import pandas as pd
from history import a
from datetime import datetime as dt

all_trips = []

for user in a:
    # first_lvl = [user["id_type"], user["serial_number"], user["is_anonymous"], user["birth_date"]]

    # i = user['contracts'][0]
    # if i['predefined_contract'] == 0:
    #     first_lvl.extend([None, None, None, None])
    # else:
    #     first_lvl.extend([i['predefined_contract'], i['is_obsolete'], i["validity_period"]["start_date"],
    #                       i["validity_period"]["end_date"]])

    trips = []
    for j in user['events']:
        all_trips.append([j["timestamp"], j["transport_mean"], j["place"], j["line_number"], j["debit_amount"]])
    # first_lvl.append(trips)

df = pd.DataFrame(all_trips, columns=['Timestamp', 'Mode', 'Place', 'Line', 'Debit_amount'])
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format=('%Y-%m-%d')).dt.date
print(df)
