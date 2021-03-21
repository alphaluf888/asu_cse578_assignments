# Graded Cell, PartID: FXGHp
# Question 2: What ride (note that not all attractions are rides) has the longest average visit time?
# Notes: Your output should be the name of the ride.
import sqlite3
import numpy as np
from datetime import timedelta
db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("select * from (SELECT attraction.name as name, \
avg(cast(substr(duration, 1,2) as integer) * 60 * 60 + cast(substr(duration, 3,5) as integer) * 60  + cast(substr(duration, 5) as integer)) \
as avg_duration FROM checkin, attraction WHERE checkin.attraction = attraction.attractionid AND category like '%Rides%' group by attraction.name) ORDER BY avg_duration desc")
resultList = c.fetchall()
print(resultList[1][0])
conn.close()