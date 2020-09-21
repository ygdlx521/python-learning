#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author  :   daliang
@Contact :   yunlianghe@appannie.com
@Software:   PyCharm
@File    :   thread_pool_executor.py
@Create  :   2020/9/14 7:58 PM
@License :   (C) Copyright 2019-2020, App Annie Inc.
@Desc    :
"""

import time
from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


def wait_n_seconds(n):
    time.sleep(n)
    return n


def func(n):
    executor = ThreadPoolExecutor(max_workers=2)
    future1 = executor.submit(wait_n_seconds, n)
    return future1


if __name__ == '__main__':
    future = func(5)
    print(future.done())
    print("finished")
    all_task = [future]
    for future in as_completed(all_task):
        data = future.result()
        print("in main: get page {}s success".format(data))
    # executor = ThreadPoolExecutor(max_workers=2)
    # future1 = executor.submit(wait_n_seconds(5))
    # future2 = executor.submit(wait_n_seconds(10))