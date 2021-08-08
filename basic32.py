# wap to compute the future value of a specified principal amount, rate of interest, and a number
# of years

p = 12000
r = 3.25
years = 3
future_value = p*((1+(0.01) * r)) ** years
print(round(future_value,2))