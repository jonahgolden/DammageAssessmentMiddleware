import pandas as pd
import numpy as np

NUM_ENTRIES = 500


types = ['fire', 'building collapse', 'partial building collapse', 'road blockage', 'medical emergency', 'power line down']
classifications = ['red', 'yellow', 'green']
intersections = pd.read_csv("data/intersections.csv")['UNITDESC']

windshield = pd.DataFrame()
windshield['intersection'] = np.random.choice(intersections, NUM_ENTRIES)
windshield['classification'] = np.random.choice(classifications, NUM_ENTRIES)
windshield['type'] = np.random.choice(types, NUM_ENTRIES)

windshield.to_csv("data/windshield.csv")
