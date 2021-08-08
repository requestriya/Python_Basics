# Write a Python program to calculate the sum of the digits in an integer.

n = 546
sum = 0
while n:
    rem = int(n%10)
    n = int(n/10)
    sum += rem
print(sum)