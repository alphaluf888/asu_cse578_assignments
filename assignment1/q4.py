# Graded Cell, PartID: B0LUP
# Question 4: Compute the Skyline of number of visits and visit time for the park's ride and
#  report the rides that appear in the Skyline.
# Notes: Remember that in this case, higher visits is better and lower visit times are better.
#  Your output should be formatted as an array listing the names of the rides in the Skyline.
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta


# a[1] is avg_visit_time which need to be minimized
# a[2] is the number_of_visits which need to be maximized
def a_dominates_b(a, b):
    if a[1] <= b[1] and a[2] >= b[2]:
        return True
    else:
        return False


def find_skylines(rowsa, rowsb):
    skylines = []
    for row_a in rowsa:
        is_dominated_by_others_flag = False
        for row_b in rowsb:
            if row_a[0] == row_b[0]:
                continue
            if a_dominates_b(row_b, row_a) == True:
                is_dominated_by_others_flag = True
                break
        if is_dominated_by_others_flag == False:
            skylines.append(row_a[0])
    return skylines


db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
# c.execute("SELECT duration, substr(duration, 1,1), substr(duration, 3,2), substr(duration, 6,2)\
# FROM checkin")
c.execute("SELECT attraction.name as name, \
avg(cast(substr(duration, 1,1) as integer) * 60 * 60 \
+ cast(substr(duration, 3,2) as integer) * 60  \
+ cast(substr(duration, 6,2) as integer))/60 \
as avg_visit_time, \
count(checkin.visitorid) as num_of_visits \
FROM checkin, attraction \
WHERE checkin.attraction = attraction.attractionid \
AND category like '%Rides%' \
and duration not like '%SD' \
group by attraction.name")
resultList = c.fetchall()
# print(resultList[0:4])
ridesArray = np.asarray(resultList)
skylines = find_skylines(ridesArray, ridesArray)
print(skylines[0:3])
conn.close()
# plt.scatter(ridesArray[:, 2], ridesArray[:,1])
# plt.show()