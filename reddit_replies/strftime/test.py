import datetime

print(datetime.date.today())
dt = datetime.datetime.strptime('2018-01-25', '%Y-%m-%d')
print(dt)                       # prints "2018-01-25 00:00:00"
print(dt.strftime('%Y-%m-%d'))  # prints only year-month-day

dt2 = datetime.date(2018, 1, 25)
print(dt2)

dt3 = datetime.datetime.strptime('2018-01-25', '%Y-%m-%d').date()
print(dt3)
