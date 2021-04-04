import sqlite3
import numpy as np
import pandas as pd
#%matplotlib inline
import matplotlib.pyplot as plt


db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute("SELECT sequence FROM sequences")
resultList = c.fetchall()
visitedAttractionList = list(map(lambda t: np.fromstring(t[0], dtype=int, sep="-").tolist(), resultList))
visitedAttractionArray = np.asarray(visitedAttractionList)

AtmosfearAttendenceTimeSeriesArray = np.count_nonzero(visitedAttractionArray == 8, axis=0)
conn.close()
#print(AtmosfearAttendenceTimeSeriesArray)
df = pd.DataFrame({'attendence': AtmosfearAttendenceTimeSeriesArray})
span = 50
df_exp = df.ewm(span=50).mean()
plt.plot(df_exp)
plt.show()