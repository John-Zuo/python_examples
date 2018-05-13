from functools import reduce


# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))
#
# res = reduce(fn, map(char2num, '13579'))
# print('map and reduce: ', res)
# print('str2int: ', str2int('13579'))
#
# # 还可以用lambda函数进一步简化成
# res = reduce(lambda x, y: x*10+y, map(char2num, '13579'))
# print('reduce with lambda: ', res)

# def is_odd(n):
#     return n % 2 == 1
#
#
# res = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# print(res)
#
# def not_empty(s):
#     return s and s.strip()
#
# res = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# print('not empty: ', res)

# 用filter求素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单
# def _odd_iter():
#     n = 1
#     while True:
#         n +=  2
#         yield n
#
# def _not_diviseble(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_diviseble(n), it)
#
#
# # 打印1000以内的素数
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
#
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 排序算法
# print('unsorted: ', [36, 5, -12, 9, -21])
# print('sorted: ', sorted([36, 5, -12, 9, -21]))
# print('sorted with reverse param: ', sorted([36, 5, -12, 9, -21], reverse=True))
# print('sorted with key param: ', sorted([36, 5, -12, 9, -21], key=abs))
#
# print('----------------')
# print('sorted: ',sorted(['bob', 'about', 'Zoo', 'Credit']))
# print('sorted with key', sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# print('sorted with key', sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 请用sorted()对上述列表分别按名字排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0].lower()
#
# L2 = sorted(L, key=by_name)
# print(L2)

# 再按成绩从高到低排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_score(t):
#     return t[1]
#
#
# L2 = sorted(L, key=by_score, reverse=True)
# print('sorted by score: ', L2)


# 函数作为返回值
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return  sum
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)
# print(f())
# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f1 == f2)
#

# 闭包
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
#
# # 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是(全部都是9)
# f1, f2, f3 = count()
# print('f1: ', f1())
# print('f2: ', f2())
# print('f3: ', f3())

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
# def count():
#     def g(i):
#         def k():
#             return i*i
#         return k
#     fs = []
#     for i in range(1, 4):
#         fs.append(g(i))
#
#     return  fs
#
# f1, f2, f3 = count()
# print('f1: ', f1())
# print('f2: ', f2())
# print('f3: ', f3())

# 利用闭包返回一个计数器函数，每次调用它返回递增整数
# 第一种方法
def createCounter():
    n = 0

    def counter():
        nonlocal n
        n += 1
        return n

    return counter


# 错误示例
# 第一种方法的变形方法, 但是是错误的，使用全局变量会导致创建第二个计数器使有副作用
# n = 0
# def createCounter():
#     def counter():
#         global n
#         n += 1
#         return n
#     return counter


# 第二种方法
# 错误的示例
# def createCounter():
#     def counter():
#         def _iter():
#             n = 0
#             while True:
#                 n = n + 1
#                 yield n
#         it = _iter()
#         return next(it)
#     return counter
#
# # 正确的示例
# def createCounter():
#     def num():
#         n = 1
#         while 1:
#             yield n
#             n = n + 1
#
#     n = num()
#     def counter():
#         return next(n)
#     return counter
# # 正确的示例
# def createCounter():
#
#     def _iter():
#         n = 0
#         while True:
#             n = n + 1
#             yield n
#     it = _iter()
#     def counter():
#         return next(it)
#     return counter
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')
#


# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量
# 所以，通过变量也能调用该函数。

# def now():
#     print('2018-5-12')
#
# f = now
# f()
# # 函数对象有一个__name__属性，可以拿到函数的名字
# print(now.__name__)
# print(f.__name__)


# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下：
# import logging
#
# def log(func):
#     def wrapper(*args, **kw):
#         logging.warning('call %s()' % (func.__name__))
#         return func(*args, **kw)
#     return wrapper
#
# # 把@log放到now()函数的定义处，相当于执行了语句：
# # now = log(now)
#
# @log
# def now():
#     print('2018-5-12')
#
# now()

# 结果
# 2018-5-12
# WARNING:root:call now()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本：
import logging

# 下面两个函数的效果貌似一样,但是不一样
# 这样写在
# @log('execute')
# def now():
#     print('2018-5-12')
# 语法糖的时候就执行print语句了,而不是实际条用now()才执行print语句
# def log(text):
#     def decoratot(func):
#         print('text: %s, call %s()' % (text, func.__name__))
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return decoratot

# 在此种情况下的根据实际效果的写法
# def log(text):
#     def decoratot(func):
#         def wrapper(*args, **kwargs):
#             logging.warning('text: %s, call %s()' % (text, func.__name__))
#             return func(*args, **kwargs)
#         return wrapper
#     return decoratot

# 这个3层嵌套的decorator用法如下
# @log('execute')
# def now():
#     print('2018-5-12')

# now

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的
# now = log('execute')(now)
# now()

# 以上两种decorator的定义都没有问题，但还差最后一步。
# 因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# print(now.__name__)

# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下
import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper
#
# # 或者针对带参数的decorator
# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# 装饰器可以定义多个，调用顺序自下而上，也就是离函数定义最近的装饰器先被调用

# def authentication(func):
#     def wrapper(*args, **kwargs):
#         print('autentication required')
#         return func()
#     return wrapper
#
#
# def limit_rate(func):
#     def wrapper(*args, **kwargs):
#         print('limit_rate')
#         return func()
#     return wrapper
#
#
# # 多个装饰器，调用顺序自下而上，执行顺序自上而下
# # 考虑语法糖帮你执行的语句
# @authentication
# @limit_rate
# def hello():
#     print('hello world!')
# hello()

# 带参数的装饰器
# import time
#
#
# def add_log(logger, timeFormat="%b %d, %Y - %H:%M:%S"):
#     def decorator(func):
#         def newFunc(*args, **kwargs):
#             logger.warning("%s Before %s() call" % (time.strftime(timeFormat), func.__name__))
#             ret = func(*args, **kwargs)
#             logger.warning("%s After %s()  call" % (time.strftime(timeFormat), func.__name__))
#             return ret
#
#         return newFunc
#
#     return decorator
#
# logger = logging.getLogger(__file__)
#
# @add_log(logger)
# def funcA():
#     print
#     "In funcA"
#
#
# @add_log(logger, timeFormat="%Y-%m-%d %H:%M:%S")
# def funcB():
#     print
#     "In funcA"
#
#
# funcA()
# funcB()

# 基于类的装饰器
# class Counter:
#     def __init__(self, func):
#         self.func = func
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#
#         return self.func(*args, **kwargs)
#
# @Counter
# def foo():
#     pass
#
#
# for i in range(10):
#     foo()
#
# print(foo.count)



