# Write a Python program to sort three integers without using conditional statements and loops.

x = 4
y = 3
z = 6

x1 = min(x, y, z)
x3 = max(x, y, z)
x2 = (x+y+z)-x1-x3

print("numbers in sorted order: ", x1, x2, x3)