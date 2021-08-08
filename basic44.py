# wap to convert height (In feet and inches) to centimeters

n = float(input('enter height in cenimeters: '))

x = n/30.48
float_format = "{:.2f}".format(x)

print(float_format + ' feet')