#   提示用户输入一个需要操作的文件路径（相对或绝对），再提示用户输入需要打印的前几行的行数。
a = input('请输入你要打开的路径:')
w = open(a,'r')
s = w.readlines()
c = len(s)
print('文件共%s行'%c)
h = int(input('你想看几行？'))
for i in s[0:h]:
    print(i,end='')
w.close()


