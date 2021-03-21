import sqlite3
import pandas as pd
#%matplotlib inline
import matplotlib.pyplot as plt

db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("SELECT a.Name, count(c.visitorID) \
FROM attraction as a, checkin c \
WHERE \
a.AttractionID = c.attraction \
AND a.Category like 'Food%' \
GROUP BY a.AttractionID \
")
foodStallsVisitsResult = c.fetchall()
print(foodStallsVisitsResult)
foodStallsVisitsDataFrame = pd.DataFrame.from_records(foodStallsVisitsResult, columns=['food_name', 'visits_count'])
c.close()
plt.bar(range(len(foodStallsVisitsDataFrame['visits_count'])), foodStallsVisitsDataFrame['visits_count'])
plt.show()