# wap to print out a set containing all the colours from color_list1
# which are not present in color_list2

color_list1 = set(['white', 'red', 'yellow', 'blue'])
color_list2 = set(['yellow', 'green', 'black', 'red']) 
color_list3 = set()
for x in color_list1:
    if x not in color_list2:
        color_list3.add(x)

print(color_list3)