import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import sqlite3
from scipy.cluster.vq import whiten
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import pandas as pd

db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute("SELECT sequence FROM sequences WHERE visitorID in (165316, 1835254, 296394, 404385, 448990)")
resultList = c.fetchall()
visitedAttractionList = list(map(lambda t: np.fromstring(t[0], dtype=int, sep="-").tolist(), resultList))
visitedAttractionArray = np.asarray(visitedAttractionList)

distanceDF = pd.DataFrame(
    squareform(pdist(visitedAttractionArray)),
    columns = [165316, 1835254, 296394, 404385, 448990],
    index = [165316, 1835254, 296394, 404385, 448990]
)

#X = np.matrix(visitedAttractionArray)
#Y = whiten(distanceDF)
#print(Y)
links = linkage(distanceDF, 'single')
dendrogram(links)
plt.show()
c.close()