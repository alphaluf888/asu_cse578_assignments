import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("SELECT a.Name, count(c.visitorID) \
FROM attraction as a, checkin c \
WHERE \
a.AttractionID = c.attraction \
AND a.Category like 'Thrill Rides%' \
GROUP BY a.AttractionID \
")
thrillRidesVisitsResult = c.fetchall()
print(thrillRidesVisitsResult)
thrillRidesVisitsDataFrame = pd.DataFrame.from_records(thrillRidesVisitsResult, columns=['ride_name', 'visits_count'])
c.close()
plt.pie(thrillRidesVisitsDataFrame['visits_count'], labels=thrillRidesVisitsDataFrame['ride_name'], autopct='%1.1f%%', shadow=False)
plt.axis('equal')
plt.show()