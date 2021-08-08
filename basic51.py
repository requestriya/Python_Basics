#83 Write a Python program to test whether all numbers of a list is greater than a certain number.
 
l = [66, 77, 89, 45, 39]
num = 36
count = 0

for item in l:
    if item > num:
        count+=1

if count == len(l):
    print('all numbers from the list are greater than ', num)
else:
    print(count, ' numbers are greater than ', num)