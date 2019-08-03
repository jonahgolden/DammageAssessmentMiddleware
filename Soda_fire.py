#!/usr/bin/env python
app_token = "t1l42B0HfErsQmTdTGrIhWaVq"

# Date ------------------------------------------------------------------------------------
from datetime import datetime, timedelta

days_to_subtract = 5

now = datetime.now()
d = (now - timedelta(days=days_to_subtract)).strftime("'%Y-%m-%dT%H:%M:%S'")

# requests ------------------------------------------------------------------------------------

import requests
import json

url = "https://data.seattle.gov/resource/kzjm-xkqj.geojson?" + "$where=datetime > " + d

params = {'where': 'datetime >'+d, 'type': 'Aid Response'}
header = {'X-App-Token': app_token}
resp = requests.request('GET', url=url, headers=header) #, params=params)

with open('data/fire_uncoded.json', 'w') as outfile:
    json.dump(resp.text, outfile)  # This dumps text as is
    #outfile.write(json.dumps(json.JSONDecoder().decode(resp.text)))  # This formats text into json



# Socrata ------------------------------------------------------------------------------------
# import pandas as pd
# from sodapy import Socrata

# # Example authenticated client (needed for non-public datasets):
# client = Socrata(domain="data.seattle.gov",
#                  app_token=app_token,
#                  username="jonahgolden@live.com",
#                  password="Riopaco1")

# # First 2000 results, returned as JSON from API / converted to Python list of
# # dictionaries by sodapy.
# query = 'SELECT datetime, type WHERE ORDER BY GROUP BY LIMIT 100 OFFSET'

# select = 'datetime, type'
# where = 'datetime > ' + d
# limit = 2000

# results = client.get(dataset_identifier="kzjm-xkqj", select=select, where=where, limit=limit)

# # Convert to pandas DataFrame

# results_df = pd.DataFrame.from_records(results)

# print(results_df.head(1000))
# print("Now: ", now)
# print("2 days ago: ", d)
# print("Results Type: ", type(results))
# ------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd
# import requests
# import json
# from pandas.io.json import json_normalize

# url = "https://data.seattle.gov/resource/kzjm-xkqj.json?"


# params = []
# data = pd.DataFrame()

# for year in list(range(2007, 2018)):
#     params.extend([{'use_code': "IND", 'assessor_neighborhood_code': "9F", 'closed_roll_year': str(year)},
#                    {'use_code': "COMO", 'assessor_neighborhood_code': "9F", 'closed_roll_year': str(year)}])

# params = [{'use_code': "IND", 'assessor_neighborhood_code': "9F", 'closed_roll_year': '2017'},
#           {'use_code': "COMO", 'assessor_neighborhood_code': "9F", 'closed_roll_year': '2017'}]

# for param in params:
#     resp = requests.get(url=url, params=param)
#     a = json.loads(resp.text)
#     res = json_normalize(a)
#     df = pd.DataFrame(res)[['use_code', 'parcel_number', 'property_area',
#                             'lot_area', 'percent_of_ownership', 'assessor_neighborhood_code', 'current_sales_date']]
#     data = data.append(df)
#     print(df.shape)