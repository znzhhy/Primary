def abc(x = 0,*args):
    if x == 'true':
        return list(reversed(sorted(args)))
    if x == 'false':
        return list(sorted(args))

a = abc('true',1,2,4,3,5)
b = abc('false',1,3,2,4,5)

print(a)
print(b)