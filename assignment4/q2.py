import sqlite3
import numpy as np
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

window_size = 50
plt.plot(np.convolve(AtmosfearAttendenceTimeSeriesArray, np.ones(window_size)/window_size, 'same'))
plt.show()