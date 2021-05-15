import pysal
import numpy as np

y = pysal.open(pysal.examples.get_path('usjoin.csv')).by_col['2009']
w = pysal.weights.rook_from_shapefile(pysal.examples.get_path('us48.shx'))
mi = pysal.Moran(y, w, two_tailed=False)
print(mi)
