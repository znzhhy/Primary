    # 定义正方形类(继承矩形类)。实现类的实例可调用，调用时打印边长;同时，直接打印类实例时能够打印出实例的面积

class Juxing:

    def __init__(self,chang,kuan):
        self.chang = chang
        self.kuan = kuan

class Zhengfangxing(Juxing):

    def __call__(self, *args, **kwargs):
        bianchang1 = self.chang + self.kuan
        bianchang2 = bianchang1 * 2
        print('边长是',bianchang2)

    def __str__(self):
        mianji = self.chang * self.kuan
        return '面积是%s'%mianji
a = Zhengfangxing(int(input('请输入第一个边长：')),int(input('请输入第二个边长：')))
a()
print(a)