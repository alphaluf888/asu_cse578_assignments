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
mean = np.nanmean(AtmosfearAttendenceTimeSeriesArray)
std = np.nanstd(AtmosfearAttendenceTimeSeriesArray)

plt.plot([0, len(AtmosfearAttendenceTimeSeriesArray)], [mean, mean], 'g-')
plt.plot([0, len(AtmosfearAttendenceTimeSeriesArray)], [mean+std, mean+std], 'y-')
plt.plot([0, len(AtmosfearAttendenceTimeSeriesArray)], [mean-std, mean-std], 'y-')
plt.plot([0, len(AtmosfearAttendenceTimeSeriesArray)], [mean+2*std, mean+2*std], 'r-')
plt.plot([0, len(AtmosfearAttendenceTimeSeriesArray)], [mean-2*std, mean-2*std], 'r-')
plt.plot(range(len(AtmosfearAttendenceTimeSeriesArray)), AtmosfearAttendenceTimeSeriesArray, 'b-')


plt.show()