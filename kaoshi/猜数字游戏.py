#   猜字游戏：最多猜10次数字的游戏，猜测范围1~100
import random

def num_fun():

    b = random.randint(1, 100)
    i = 0

    while i < 10:

        i += 1
        a = int(input('请输入你所猜的数字（仅限1-100整数）：'))
        if a == b:
            print('恭喜你，猜对了!你猜了%s次'%i)
            break
        elif  a < b:
            print('不对哟，你猜的小了！你猜了第%s次哦！'%i)
        elif  a > b:
            print('不对哟，你猜的大了！你猜了第%s次哦！'%i)

    else:
        print('很遗憾，你的次数已用光！正确答案是：%s'%b)

num_fun()