# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function

l1 = [45, 78, 34, 56, 105, 60, 44]

result = list(filter(lambda x: (x % 15 == 0), l1))

print('numbers of the said list divisible by 15 are: ', result)
