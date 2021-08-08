# Write a Python program to check whether a string is numeric.
# 1.
val = '12345'
count = 0
for i in val:
    if (ord(i)>=48 and ord(i)<=57):
        count+=1
    else:
        print('has alpha values')
        break

if count == len(val):
    print('val has only numeric value')

# 2.
if val.isdigit():
    print('its numeric')
else:
    print('has alpha')