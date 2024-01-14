from datetime import datetime

date = datetime.now()
print(date)
print(type(date))
isodate = datetime.isoformat(date)
print(isodate)
print(type(isodate))
