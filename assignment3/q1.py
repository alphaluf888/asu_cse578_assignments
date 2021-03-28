import sqlite3
import numpy as np
#import pandas as pd
#%matplotlib inline
#import matplotlib.pyplot as plt

db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("SELECT sequence FROM sequences WHERE visitorID IN (165316, 1835254, 296394, 404385, 448990)")
resultList = c.fetchall()
vistedAttractionList = list(map(lambda t: np.fromstring(t[0], dtype=int, sep="-").tolist(), resultList))
vistedAttractionArray = np.asarray(vistedAttractionList)
#print(vistedAttractionArray.shape)
visitorIds = [165316, 1835254, 296394, 404385, 448990]
disSimilarityMatrixDict = {}

for i in range(5):
    rowDisSimilarityDict = {}
    for j in range(5):
        if i != j:
            disSimilarityArray = vistedAttractionArray[i, :] != vistedAttractionArray[j, :]
            (unique,counts) = np.unique(disSimilarityArray, return_counts=True)
            #print((unique,counts))
            if len(counts) == 1:
                rowDisSimilarityDict[visitorIds[j]] = 0
            else:
                rowDisSimilarityDict[visitorIds[j]] = counts[1]
    disSimilarityMatrixDict[visitorIds[i]] = rowDisSimilarityDict

c.close()
print(disSimilarityMatrixDict)