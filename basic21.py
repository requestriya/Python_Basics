# wap to concatenate all elements in a list into a string and return it.

def concate(args):
    con = ''
    for i in args:
        con = con + ' ' + i
    return str(con)

print(concate(['riya', 'singh','got', 'cake']))