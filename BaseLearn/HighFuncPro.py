# -*- coding:utf-8 -*-
# 函数式编程之高阶函数
from functools import reduce


def f(x):
    return x * x


def add(x, y):
    return x + y


def is_odd(n):
    return n % 2 == 1


# map()两个参数: 一个f,一个Iterable,把Iterable中的每个元素都执行f,最后返回Iterator
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  # 返回的是Iterator惰性序列，用list计算出来
print(list(r))

# reduce()两个参数,同map,把结果继续和序列的下一个元素做累积计算
print(reduce(add, [1, 3, 5, 7, 9]))

# filter()也接受一个函数和一个序列返回的是一个Iterator,把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 排序算法sorted(),可以接收一个key函数来实现自定义的排序
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  # 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
