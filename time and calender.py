#time module
import time
print(time.time())
print(time.ctime())
print(time.localtime())
print(time.gmtime())
print(time.asctime())
print(time.strftime("%d.%m.%y"))
print(time.strftime("%d-%m-%y"))
print(time.mktime(time.localtime()))
print(time.perf_counter())


#calender module
import calendar
print(calendar.calendar(2026))
print(calendar.month(2100,7))
print(calendar.monthrange(2026, 7))
print(calendar.isleap(2023))
print(calendar.leapdays(2000,2024))
print(calendar.weekday(2026,7,8))
print(calendar.month_name[7])
print(calendar.day_name[2])
