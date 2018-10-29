# 写一个用于装饰函数的装饰器，用来统计一个函数执行的次数。
# 效果：每次执行完该函数以后，立即打印该函数执行的次数。

def hangshu(s):
    n = 0
    def shu(*args,**kwargs):
        nonlocal n
        s(*args,**kwargs)
        n += 1
        print('函数执行了%s次'%n)
    return shu

@hangshu
def fun_1():
    for i in range(1,3):
        print('第%i次'%i)

fun_1()
fun_1()
fun_1()