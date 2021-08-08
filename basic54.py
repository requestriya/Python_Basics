# define a string that has alphanumeric letters and print only alphabet from that string

dec = 'ABc5d90uibdy56h38$!a'

for i in dec:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        print(i, end=' ')

