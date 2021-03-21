# Graded Cell, PartID: NDnou
# Question 1: What is the most popular attraction to visit in the park?
# Notes: Your output should be the name of the attraction.
import sqlite3
import numpy as np
db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("SELECT sequence FROM sequences")
resultList = c.fetchall()
uniqueVistedAttractionList = []

list(map(lambda t: uniqueVistedAttractionList.extend(np.unique(np.fromstring(t[0], dtype=int, sep="-")).tolist()), resultList))
#print(uniqueVistedAttractionList)
uniqueVistedAttractionNArray = np.asarray(uniqueVistedAttractionList)
mostVisitedAttractionId = np.bincount(uniqueVistedAttractionNArray[uniqueVistedAttractionNArray != 0]).argmax()
#print(mostVisitedAttractionId)
c.execute("SELECT name FROM attraction WHERE attractionid = {0}".format(mostVisitedAttractionId))
print(c.fetchone()[0])
conn.close()