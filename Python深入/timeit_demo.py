#! usr/bin/env python3
# coding=utf-8

import timeit


def func():
    for i in range(10):
        print(i)


res = timeit.Timer(func).timeit(100)
print(res)
