# wap a program to count the number 4 in a given list
list1 = [3, 6, 8, 4, 9, 0, 4, 9, 4]
count = 0

for num in list1:
    if num == 4:
        count += 1


print(count)