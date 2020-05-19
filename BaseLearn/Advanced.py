# -*- coding:utf-8 -*-
from collections import Iterable


def trim(s):  # 去首位空字符
    if len(s) == 0:
        return s
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-2])
    else:
        return s


def item_test():  # 迭代
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key)
    for value in d.values():
        print(value)
    for k, v in d.items():
        print(k, ':', v)
    print(isinstance('abc', Iterable))  # 判断str是否可以迭代
    print(isinstance([1, 2, 3], Iterable))  # 判断一个list是否可以迭代
    print(isinstance(123, Iterable))  # 整型是否可以迭代
    # enumerate把list变成索引-元素对形式
    for i, value in enumerate(['a', 'b', 'c']):
        print(i, value)
    #  一个for循环引用两个变量
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)


def List_create():  # 列表生成器
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print([x * x for x in range(1, 11)])  # 生成元素 for 迭代元素 in list
    print([x * x for x in range(1, 11) if x % 2 == 0])  # 生成元素 for 迭代元素 in list if 筛选条件
    print([k + '=' + v for k, v in d.items()])
    print([x if x % 2 == 0 else -x for x in range(1, 11)])


def generator():  # 生成器
    g = (x * x for x in range(10))  # 和列表生成器的区别 [] -> ()
    for n in g:
        print(n)
