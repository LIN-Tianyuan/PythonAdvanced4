# Import libraries
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType

import pandas as pd
# import data
dataset = pd.read_csv('owid-covid-data.csv')
print(dataset.head())
