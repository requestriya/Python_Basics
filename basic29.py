# wap that will return true if the two given integers values are equal or their sum or difference is 5

def eq(x, y):
    sum = x+y
    diff = abs(x-y)
    if ((x==y) or (sum == 5) or (diff == 5)):
        return True
    return False

print(eq(15, 5))
print(eq(5, 5))
print(eq(0, 5))
print(eq(5, 10))