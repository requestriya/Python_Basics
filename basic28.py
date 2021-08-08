# wap to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

def equation(x, y):
    sum = x+y
    if (sum>=15 and sum<=20):
        sum = 20
    return sum

print(equation(2,5))
print(equation(15, 3))