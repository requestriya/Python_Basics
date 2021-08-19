# wap to input a number, if it is not a number generates and error message

while True:
    try:
        a = int(input("input a number: "))
        break
    except ValueError:
        print("\n This is not a number. Try again...")
        print()