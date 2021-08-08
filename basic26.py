# wap to compute the greatest common divisor (GCD) of two positive integers.

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z+=1
    return lcm

print(lcm(4,7))
print(lcm(8,4))