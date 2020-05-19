# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 22:53
# @Author  : Wu Tianyu
# IO学习
from io import StringIO
import os
import pickle
import json


# 读文件
def readFile():
    # try:
    #     f = open('E:\\实用的网站.txt', 'r',encoding='utf-8', errors='ignore')
    #     r 表示读,rb表示读二进制文件(图片和视频等)
    #     print(f.read())
    # finally:
    #     if f:
    #         f.close()

    """
    read()会读取全部文件,内存浪费
    read(size)读取size字节的内容
    readline()每次读取一行
    readlines()一次读取返回一个list
    """
    with open('E:\\实用的网站.txt', 'r') as f:  # 精简版本,with自动帮我们调用close

        for line in f.readlines():
            print(line.strip())


# 写文件
def writeFile():
    with open('E:\\test.txt', 'w') as f:  # w 表示写文件 文件若存在则会被覆盖, a 表示追加写入
        f.write("Hello World")


# StringIO
def StringIOFile():
    f = StringIO()
    f.write("Hello World")
    print(f.getvalue())  # getValue用于获得写入后的str


# os 操作文件与目录
def OSFile():
    print(os.name)  # 操作系统名
    print(os.environ)  # 环境变量
    print(os.environ.get('path'))  # 获取特定环境变量
    print(os.path.abspath('.'))  # 获取当前目录的绝对路径
    print(os.path.join('D:\\', 'testDir'))  # 拼接完整路径
    print(os.path.split("E:\\实用的网站.txt"))  # 路径拆分为两个部分(后一部分总是最后级别的目录或文件名)
    print(os.path.splitext("F:\\迅雷\\Thunder\\补丁\\补丁使用方法.txt"))  # 以直接让你得到文件扩展名
    os.mkdir("D:\\testDir")  # 创建新的目录
    os.rmdir("D:\\testDir")  # 删除目录
    os.rename("", "")  # 对文件重命名
    os.remove("")  # 删除文件


# 序列化:我们把变量从内存中变成可存储或传输的过程称之为序列化,把变量内容从序列化的对象重新读到内存里称之为反序列化
def pickleL():
    d = dict(name='Bob', age=20, score=88)
    f = open("E:\\pickle.txt", 'wb')
    pickle.dump(d, f)  # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
    f.close()


# 反序列化
def pickleRe():
    f = open("E:\\pickle.txt", 'rb')
    d = pickle.load(f)
    f.close()
    print(d)


# py 转 json
def PyToJson():
    d = {'name': 'Bob', 'age': 20, 'score': 88}
    print(json.dumps(d))


"""
对象转json
"""


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def StudentToJson(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def StudentToJsonTest():
    stu = Student("Bob", 22, 88)
    print(json.dumps(stu, default=StudentToJson))


if __name__ == '__main__':
    # readFile()
    # writeFile()
    # StringIOFile()
    # OSFile()
    # pickleL()
    # pickleRe()
    # PyToJson()
    StudentToJsonTest()
