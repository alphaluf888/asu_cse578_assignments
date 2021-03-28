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
vistedAttractionList = list(map(lambda t: np.fromstring(t[0], dtype=int, sep="-").tolist(), resultList))
vistedAttractionArray = np.asarray(vistedAttractionList)

c.execute("SELECT AttractionID FROM attraction WHERE Category like '%Rides%'")
resultList = c.fetchall()
ridesList = list(map(lambda t: t[0], resultList))
ridesArray = np.asarray(ridesList)
c.close()

ridesAttendenceResultArray = np.zeros((ridesArray.shape[0], vistedAttractionArray.shape[1]))
#ridesAttendenceResultArray = np.insert(ridesAttendenceResultArray, 0, ridesArray, axis=1)
#print(ridesAttendenceResultArray)

for i in range(vistedAttractionArray.shape[1]):
    (unique, counts) = np.unique(vistedAttractionArray[:, i], return_counts=True)
    freqArray = np.asarray((unique, counts)).T
    for f in freqArray:
        index = np.where(ridesArray == f[0])
        if index[0].size > 0:
            ridesAttendenceResultArray[index[0][0], i] = f[1]

#print(ridesAttendenceResultArray)
finalResultArray = np.zeros((ridesArray.shape[0], 3))

ridesAttendenceResultArray[ridesAttendenceResultArray == 0] = np.nan
#print(ridesAttendenceResultArray)

minArray = np.nanmin(ridesAttendenceResultArray, axis=1)
#print(minArray)
maxArray = np.nanmax(ridesAttendenceResultArray, axis=1)
#print(maxArray)
avgArray = np.nanmean(ridesAttendenceResultArray, axis=1)
#print(avgArray)

#finalResultArray = np.insert(finalResultArray, 0, ridesArray, axis=1)
finalResultArray = np.zeros((ridesArray.shape[0], 4))
finalResultArray[:, 0] = ridesArray
finalResultArray[:, 1] = minArray
finalResultArray[:, 2] = avgArray
finalResultArray[:, 3] = maxArray
#print(finalResultArray)
df = pd.DataFrame(finalResultArray[:,1:], columns=['min', 'average', 'max'])
#print(df)
#print(df)
pd.plotting.scatter_matrix(df)
plt.show()