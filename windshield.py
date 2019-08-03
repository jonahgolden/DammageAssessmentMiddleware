import pandas as pd
import numpy as np
import json

NUM_ENTRIES = 500

# Getting some intersections from fire data
with open('data/fire_formatted.json') as data_file:    
    data = json.load(data_file)

df = pd.DataFrame(data["features"])
df = df["properties"]

# Only want addresses with '/', which indicates an intersection
fire_inters = pd.DataFrame([d['address'] for d in df if " / " in d['address']])

# Getting some intersections from Seattle Open Data
other_inters = pd.read_csv("data/intersections.csv")['UNITDESC']

# Combining intersections from both sources
intersections = pd.DataFrame(np.random.choice(other_inters, NUM_ENTRIES - fire_inters.size)).append(fire_inters)

# Defining some types and classification enums
types = ['fire', 'building collapse', 'partial building collapse', 'road blockage', 'medical emergency', 'power line down']
classifications = ['red', 'yellow', 'green']

# Combining intersections, classifications, and types randomly
windshield = pd.DataFrame()
windshield['intersection'] = np.random.choice(intersections.iloc[:,0], NUM_ENTRIES)
windshield['classification'] = np.random.choice(classifications, NUM_ENTRIES)
windshield['type'] = np.random.choice(types, NUM_ENTRIES)

# Saving as csv file
windshield.to_csv("data/windshield.csv")
