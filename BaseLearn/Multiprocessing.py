# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 20:26
# @Author  : Wu Tianyu
# 多进程与多线程
import os
import random
import time
import threading
from multiprocessing import Pool
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def process():
    print("父类进程%s" % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 目标子进程和参数
    print('Child process will start.')
    p.start()  # 启动
    p.join()  # 等待子进程结束后
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# 进程池
def processPool():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 设置池上限，最多同时执行4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()
    print('All subprocesses done.')


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def threadLearn():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    # process()
    # processPool()
    threadLearn()
