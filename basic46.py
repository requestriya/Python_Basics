# wap to convert all unit of times into seconds
hour = int(input('enter the hour : '))
minute = int(input('enter the minute : '))

hour_in_sec = int((hour*60)*60)
min_in_sec = int(minute*60)
total = hour_in_sec + min_in_sec

print('total second = ',  total)
