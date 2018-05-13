# encoding: utf-8

import time


# 限制函数在指定时间内只运行一次, 第一次直接调用的时候无反应
def time_guard(time_interval, default=None):
    def decorator(func):
        # 记录时间应该放在这里
        func.__last_run = time.time()

        def guard(*args, **kwargs):
            now = time.time()
            if now - func.__last_run > time_interval:
                func.__last_run = now
                return func(*args, **kwargs)
            elif default is not None:
                return default(*args, **kwargs)

        return guard

    return decorator


def count_guard(time_interval, count, default=None):
    def decorator(func):
        func.__count = 0
        def guard(*args, **kwargs):
            if  func.__count < count:
                func.__count += 1
                return func(*args, **kwargs)
            elif default is not None:
                return default(*args, **kwargs)
        return guard

    return decorator


if __name__ == '__main__':

    @time_guard(time_interval=2)
    def add():
        print('execute add')


    time.sleep(3)
    for i in range(5):
        print('index i = ', i)
        add()
        time.sleep(1)

"""
    for i in range(5):
        print('index i = ', i)
        add()
        time.sleep(1)
# 执行结果如下， 可以看到第一次调用add时没有立马执行，而是
# index i =  0
# index i =  1
# index i =  2
# execute add
# index i =  3
# index i =  4
# execute add

"""

"""
    time.sleep(3)
    for i in range(5):
        print('index i = ', i)
        add()
        time.sleep(1)
# 结果
index i =  0
execute add
index i =  1
index i =  2
execute add
index i =  3
index i =  4
execute add

"""
