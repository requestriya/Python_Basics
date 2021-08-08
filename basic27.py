# wap to sum of three numbers given integers. however, if two values are equal sum will be zero
 
def sum_nums(n1, n2, n3):
    if (n1 == n2 or n1 == n3 or n2 == n3):
        sum = 0
    else:
        sum = n1+n2+n3
    return sum

print(sum_nums(2,4,5))
print(sum_nums(2,2,2))