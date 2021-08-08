# wap to sum of the first n positive integers

n = int(input('enter the n value : '))

sum = 0

for x in range(1,n+1):
    sum += x

print(sum)