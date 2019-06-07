import pandas as pd

print(pd.__version__)

auto_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data', sep=r'\s*,\s*', engine='python')
print(auto_data)


#replace ? with nan

import numpy as np

auto_data = auto_data.replace('?', np.nan)
auto_data.head()
print(auto_data)

auto_data.describe(include='all')  # give overview on data

#print(auto_data['price'].describe())


auto_data = auto_data.drop('normalized-losses', axis=1)
res2 = auto_data.head()

print(res2)