import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pysal as ps

#world = gpd.read_file(gpd.datasets.get_path())

us_income = pd.read_csv(ps.examples.get_path('usjoin.csv'))
print(us_income)

us_income_shape = gpd.read_file(ps.examples.get_path('us48.shx'))

#us_income_shape.plot()