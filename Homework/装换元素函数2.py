def exchange(tu,di):
    li = []
    for i in list(di.keys()): # 循环字典的所有key
        li.append(di[i]) # 将字典的value添加到列表

    new_di = dict(zip(di.keys(),tu))
    new_tu = tuple(li)
    return new_tu,new_di

a = exchange((1,2,3),{'a':555,'b':222,'c':666})
print(a)