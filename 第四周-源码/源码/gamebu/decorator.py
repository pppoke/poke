# Author:Game_bu

import time, functools, sys


def decorator(name):
    def out_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            print("name:", name)
            start_time = time.time()
            ret = func(*args, **kwargs)
            stop_time = time.time()
            print("the time for run test is {_time}".format(_time=stop_time - start_time))
            return ret
        # wrapper.__name__ = func.__name__
        return wrapper
    return out_wrapper


@decorator("I'm func1")  # func1 = decorator("I'm func1")(func1)=out_wrapper(func1)=wrapper
def func1(x, y):
    print("x+y=", x+y)
    time.sleep(1)
    print("wwwwwwwwwwwwwww")
    return 11


@decorator("I'm func2")  # func1 = decorator("I'm func2")(func2)=out_wrapper(func2)=wrapper
def func2(x, y):
    print("x+y=", x+y)
    time.sleep(5)
    print("aaaaaa")
    return 22

print(func1.__name__)
func1(2, 900)

print(id(func1))

hash('刘剑波')

print(5>>1)
a = 'qwert'
l = [1,2,3,4]
b = reversed(l)
for i in b:
    print(i)

print()