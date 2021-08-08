# wap to accept filname from the user and print the extension of that

file_name = input('enter file name ')

fextns = file_name.split('.')
print('extension is ' + repr(fextns[-1]))
