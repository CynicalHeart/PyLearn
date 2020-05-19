import math


#  参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')  # 错误提示
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  # 返回的其实是一个tuple


def quadratic(a, b, c):  # 一元二次方程解
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


def power(x, n=2):  # 复现pow功能
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 默认参数理解
def enroll(name, gender, age=6, city='Beijing'):
    print(name)
    print(gender)
    print(age)
    print(city)


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def calc(*number):  # 加*号可变参数list or tuple
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


def person(name, age, **kw):  # **kw代表关键字参数 用dict装入，kw获得的是一份拷贝，这里面的改动不会改变外面的情况
    if "city" in kw:
        pass
    if "job" in kw:
        pass
    print("name:", name, "age:", age, "other:", kw)


def person2(name, age, *, city="北京", job):  # 限制关键字的输入,用*号做特殊分隔符号,后面的参数被视作关键字参数
    print(name, age, city, job)


def product(*param):
    if len(param) == 0:
        raise TypeError
    sum = 1
    for num in param:
        sum = sum * num
    return sum


def fact(n):  # 普通递归
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, pro):
    if num == 1:
        return pro
    return fact_iter(num - 1, num * pro)
