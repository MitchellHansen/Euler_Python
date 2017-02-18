import time
from time import gmtime, strftime, struct_time
from datetime import date, datetime, timedelta
import datetime
import re


d = datetime.datetime(1901,1,1,0,0,0).timetuple()

print(strftime("%a, %d %b %Y %H:%M:%S +0000", d))



def datespan(startDate, endDate, delta=timedelta(weeks=1)):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

span = datespan(date(1901, 1, 1), date(2000, 12, 31))

days = 0;

for i in span:
    split = str(i).split('-')
    day = int(split[2])

    if day == 1:
        days += 1

print(days)