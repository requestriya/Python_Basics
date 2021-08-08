# wap to print all even numbers from a given numbers list in the same
# order and stop the printing if any numbers that come after 237 in the sequence.

list1 = [234, 67, 54, 55, 34, 32, 899, 567, 345, 222]

for x in list1:
    if (x>237):
        break
    else:
        if (int(x)%2==0):
            print(x)

    