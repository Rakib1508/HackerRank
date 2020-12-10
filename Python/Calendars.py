import calendar

days = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')
month, date, year = map(int, input().split(' '))
day = calendar.weekday(year, month, date)
print(days[day])
