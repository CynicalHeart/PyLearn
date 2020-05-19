# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 21:34
# @Author  : Wu Tianyu
from types import MethodType
from enum import Enum, unique


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # __str__ 自定义
        return "Student object(name %s)" % self.name

    __repr__ = __str__  # __repr__()返回程序开发者看到的字符串,给变量显示用的

    def __getattr__(self, item):  # 调用不存在属性的时候，只有在没有找到属性的情况下，才调用__getattr__
        if item == 'score':
            return 98


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


# 枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


def iter_Month():
    for name, member in Month.__members__.items():
        print(name, "=>", member, ",", member.value)


@unique
class Weekday(Enum):  # 周枚举类
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问枚举类
def visitEnum():
    day1 = Weekday.Sun
    print(day1)
    print(Weekday(1))
    print(Weekday.Thu)
    print(Weekday.Thu.value)


def set_age(self, age):
    self.age = age


# 给实例绑定一个方法
def bangMethod():
    s = Student()
    s.set_age = MethodType(set_age, s)
    s.set_age(24)
    print("给实例绑定的年龄方法", s.age)


# 给一个类绑定方法
def bangMethodClass():
    Student.set_age = set_age
    s1 = Student()
    s2 = Student()
    s1.set_age(24)
    print(s1.age)
    s2.set_age(26)
    print(s2.age)


# 使用__slots__限制实例属性 注：只对当前类生效,不对子类生效
class Person(object):
    __slots__ = ("name", "age")  # 用tuple定义允许绑定的属性名称


# __str__ 自定义类
def class_str():
    print(Student("吴天宇"))


# __iter__和 __next__
def class_iter():
    for n in Fib():
        print(n)


if __name__ == '__main__':
    # class_str()
    # class_iter()
    # iter_Month()
    visitEnum()
