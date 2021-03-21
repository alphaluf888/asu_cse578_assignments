import sqlite3
import pandas as pd
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
def generate_visit_timelist(v):
    return [v, v]
db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("SELECT sequence FROM sequences")
resultList = c.fetchall()

vistedAttractionList = list(map(lambda t: np.fromstring(t[0], dtype=int, sep="-").tolist(), resultList))
vistedAttractionArray = np.asarray(vistedAttractionList)
atmosfearVisits = np.count_nonzero(vistedAttractionArray[:,0:192] == 8, axis=0)
atmosfearVisitsDataFrame = pd.DataFrame(atmosfearVisits)
atmosfearVisitsDataFrame.insert(0, 'time', ["t+"+str(i) for i in range(192)])
print(atmosfearVisitsDataFrame.values.tolist())
lines = atmosfearVisitsDataFrame.plot.line()
plt.show()
c.close()


