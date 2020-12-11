import datetime
import time

#date method

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.date.today())
print(datetime.date(2020, 4, 28))
print(datetime.datetime.today())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.max)
d = datetime.date.today()
print(d.year)
print(d.month)
print(d.day)
d = d.replace(month = 12, day = 5)
print(d)
print(d.timetuple())
print(d.weekday())
print(d.isocalendar())
print(d.isoformat())
print(d.ctime())
print(d.resolution)

#time method

t = datetime.time(10, 59, 20, 9999)
print(t)
print(t.resolution)

print(t.replace(hour = 5, minute = 5, second = 5))
print(t)
print(t.isoformat())
print(t.__str__())

print(datetime.datetime.now())
d = datetime.datetime.utcnow()
print(d.date())
print(d.time())
td = datetime.timedelta(365, 50, 55555, 411111, 2, 20, 5)
print(td)

print(time.asctime())