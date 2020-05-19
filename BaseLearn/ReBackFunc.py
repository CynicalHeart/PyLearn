# -*- coding:utf-8 -*-
# 返回函数


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def build(x, y):
    return lambda: x ** 2 + y ** 2


# 返回函数,当调用时返回的函数时才会进行计算
f = lazy_sum(1, 3, 5, 7, 9)
print(f())

# 每次调用都会返回一个新的函数，即使传入的参数相同
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

# 匿名函数 lambda函数---lambda (函数参数): 表达式
# 匿名函数有个限制,就是只能有一个表达式,返回值就是该表达式的结果。
func3 = lambda x: x ** 3
print(func3(5))
print(build(2, 3))
