# *coding:utf-8 *
lst = [{11: 22, 22: 33, 33: 44}, {11: 33, 22: 323, 33: 424}, {11: 44, 22: 313, 33: 414}]

i = 22
lst.sort(key=lambda x: int(x[i]), reverse=False)     # lambda 匿名函数 表达式
print(lst)

print('------------------2种方法排序------------------------------')


def comp(_i):   # 列表内的字典匿名
    return _i[22]


lst.sort(key=comp, reverse=False)
print(lst)

# 按升序对列表排序，不返回任何值。
#
# 排序已就位（即列表本身已修改）且稳定（即保持两个相等元素的顺序）。
#
# 如果给定了一个键函数，则对每个列表项应用一次，并根据它们的函数值对它们进行升序或降序排序。
#
# 反向标志可以设置为按降序排序
