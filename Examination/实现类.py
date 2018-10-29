# 背景：我们人类处于生物金字塔的顶端，都有着名字，职业、会吃饭，睡觉。
# 需求：请实现一个学生类，它能够学习和自我介绍。

class Human:
    def __init__(self,name,job):
        self.name = name
        self.job = job
    def eat(self):
        print('%s在吃饭'%self.name)
    def sleep(self):
        print('%s在睡觉'%self.name)
class  Student(Human):
    def study(self):
        print('%s在学习'%self.name)
    def introduce(self):
        print('我叫%s,我是%s'%(self.name,self.job))


Human('张三','医生').eat()
Human('张三','医生').sleep()
Student('李四','学生').study()
Student('李四','学生').introduce()