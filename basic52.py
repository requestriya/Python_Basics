# 84. Write a Python program to count the number occurrence of a specific character in a string.

name = 'helloooo'
gather = ''


for x in range(len(name)):
    i = 1
    if name[x] not in gather:
        gather += name[x]
        for j in range(x+1, len(name)):
            if name[x] == name[j]:
                i+=1
        print(name[x], ' occured: ', i)
    
    
