#定义一个函数，可以对传入的数据进行排序，通过一个参数来决定是正向排序还是反向排序
#给定的参数个数为奇数倒序排列，个数为偶数正序排列。
def test_p(*args):
    a = sorted(args)
    print(a)
    return list(a) if len(args) % 2 == 0 else list(reversed(a))

c = list(test_p(3,4,2,6,5,7,1))
print(c)