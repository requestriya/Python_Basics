# wap to calculate the sum of three given numbers, if the values are equal then return thrice of their sum


def thrice_sum(n1, n2, n3):
    sum = n1 + n2 + n3

    if n1 == n2 == n3:
        sum = sum * 3
    return sum


total = thrice_sum(5, 5, 5)
print(total)


