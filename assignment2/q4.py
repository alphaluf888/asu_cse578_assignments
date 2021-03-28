import sqlite3
import pandas as pd
#%matplotlib inline
import matplotlib.pyplot as plt

db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("SELECT count(c.visitorID) \
FROM attraction as a, checkin c \
WHERE \
a.AttractionID = c.attraction \
AND a.Category like 'Kiddie Rides%' \
GROUP BY a.AttractionID \
")
kiddieRidesVisitsResult = c.fetchall()

kiddieRidesVisitsDataFrame = pd.DataFrame.from_records(kiddieRidesVisitsResult, columns=['visits_count'])
print(kiddieRidesVisitsDataFrame.values.flatten().tolist())
c.close()
plt.boxplot(kiddieRidesVisitsDataFrame['visits_count'], labels=["Kiddie Rides Visits"])
plt.show()