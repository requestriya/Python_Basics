# wap that accepts an integer(n) and computes the value n+nn+nnn

n = int(input('enter and integer: '))
n1 = int('%s' % n)
n2 = int('%s%s' % (n,n))
n3 = int('%s%s%s' % (n,n,n))

print(n1+n2+n3)



