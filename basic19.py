# wap to check whether a specified value is contained in a group of values.

def check(n):
    list_value = [2,5,7,8,7,5]
    if n in list_value:
        return 'it is present in the list'
    return 'its not in the list'

print(check(2))

