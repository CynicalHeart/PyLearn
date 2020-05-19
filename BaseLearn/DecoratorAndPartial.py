# -*- coding:utf-8 -*-
# 装饰器和偏函数


# 在函数调用前后自动打印日志，但又不希望修改函数的定义，在代码运行期间动态增加功能的方式称之为“装饰器”
import functools


def log(func):
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)

    return wrapper


@log  # 相当于执行了now = log(now)
def now():
    print("2020-4-26")


now()

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值）,返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)
print(int2('101010'))
