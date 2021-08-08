# wap to calculate number of days between two dates.

date1 = (2013, 3, 11)
date2 = (2014, 7, 11)

day = date1[-1]-date2[-1]
month = (date1[1]-date2[1]) * 30
year = (date1[0]-date2[0]) * 365
total = day+month+year

print('total days are : %s' % abs(total))