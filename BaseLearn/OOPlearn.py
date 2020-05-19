# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 13:26
# @Author  : Wu Tianyu


# 面向对象基础学习
class Student(object):  # ()中表示继承于哪个类,object所有类都会继承
    tag = "Student"  # 绑定类的属性，所有对象都能访问到

    def __init__(self, name, score):  # init 第一个参数永远是self,表示实例本身,
        self.__name = name  # __私有属性
        self.__score = score  # __私有属性

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):  # 这种方法可以对参数进行检测
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print("%s %s" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


class Animal(object):
    def run(self):
        print("Animal is running....")


class Dog(Animal):  # 继承类
    def run(self):
        print("Dog is running...")


class Cat(Animal):
    def run(self):
        print("Cat is running...")


if __name__ == '__main__':
    print("call 主函数")
    print(Student.tag)  # 实例属性优先级高于类属性
    # 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
    dog = Dog()
    cat = Cat()
    dog.run()
    cat.run()
    print("-----------------------------------------------------")
    # type的使用:它返回对应的Class类型
    print(type(dog))
    # isinstance 判断是否从属类别,
    print(isinstance(cat, Animal))
    # 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
    print(isinstance([1, 2, 3], (list, tuple)))
    # 获得一个对象的所有属性和方法,可以使用dir()函数,它返回一个包含字符串的list
    print(dir(Animal))
    # hasattr(obj, 'x')判断对象有x属性吗
    # setattr(obj, 'y', 19) 给对象设置一个y值为19
    # getattr(obj, 'y') 获得对象属性为y的值
