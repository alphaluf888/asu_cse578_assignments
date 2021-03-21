# Graded Cell, PartID: KALua
# Question 3: Which Fast Food offering in the park has the fewest visitors?
# Notes: Your output should be the name of the fast food offering.
import sqlite3
import numpy as np
db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("SELECT attractionid FROM attraction WHERE type = 'Fast Food'")
resultList = c.fetchall()
fastFoodList = list(map(lambda t: t[0], resultList))
#print(fastFoodList)

c.execute("SELECT sequence FROM sequences")
resultList = c.fetchall()
uniqueVistedAttractionList = []

list(map(lambda t: uniqueVistedAttractionList.extend(np.unique(np.fromstring(t[0], dtype=int, sep="-")).tolist()), resultList))
#uniqueVistedAttractionArray = np.asarray(uniqueVistedAttractionList)
visitedFastFoodList = []
list(map(lambda a: visitedFastFoodList.append(a) if a in fastFoodList else None, uniqueVistedAttractionList))
#print(visitedFastFoodList)
uniqueVisitedFastFoodId, counts = np.unique(visitedFastFoodList, return_counts=True)
fewestVisitedFastFoodId = uniqueVisitedFastFoodId[counts.argmin()]
#print(fewestVisitedFastFoodId)
c.execute("SELECT name FROM attraction WHERE attractionid = {0}".format(fewestVisitedFastFoodId))
print(c.fetchone()[0])
conn.close()