# 有如下列表：
# li = ['Hello','i',["Python",[('潭州'),'Love'],'无名'],'嘤嘤嘤']
# 结合索引，找出其中对应位置的数据，最后打印出Hello 潭州 无名 I Love Python。
li = ['Hello','i',["Python",[('潭州'),'Love'],'无名'],'嘤嘤嘤']

print(li[0],li[2][1][0],li[2][2],li[1].upper(),li[2][1][1],li[2][0],'。')