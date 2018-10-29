#定义一个函数，传入一个字典和一个元组，将字典的值和元组的值交换，返回交换后的字典和元组
def test(z,y):
    print('原来的字典',z)
    print('原来的元组',y)
    p = list(z.keys())
    x = dict(zip(p,y))
    q = tuple(z.values())
    print('新的字典',x)
    print('新的元组',q)

i = {'a':1,'b':2,'c':3}
j = (4,5,6)

test(i,j)