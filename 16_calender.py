# import calendar
# # print(calendar.month(2024, 1)) # January 2024

# for i in range(1,13):
#     print(calendar.month(2025,i))


import calendar

month,day,year = map(int,input().split())
day = calendar.weekday(year,month,day)
day_upper = calendar.day_name[day].upper()
print(day_upper)
