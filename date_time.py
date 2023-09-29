from datetime import datetime

now = datetime.now()
print(now)
month = now.month
print(month)
year = now.year
print(year)

day = now.day
print(day)

day_of_week = now.weekday()
print(day_of_week)

now = datetime(year=2002, month=10, day=20, hour=12)
print(now)
