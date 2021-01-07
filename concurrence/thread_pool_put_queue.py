#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author  :   daliang
@Contact :   yunlianghe@appannie.com
@Software:   PyCharm
@File    :   thread_pool_put_queue.py
@Create  :   2020/12/29 2:24 PM
@License :   (C) Copyright 2019-2020, App Annie Inc.
@Desc    :
"""
import datetime
from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue

queue = Queue(128)


def put_into_queue(num):
    print(str(datetime.datetime.now()) + "start current qsize: " + str(queue.qsize()) + "\n")
    queue.put(num)
    print(str(datetime.datetime.now()) + "end current qsize: " + str(queue.qsize()) + "\n")



if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=8) as executor:
        while True:
            executor.submit(put_into_queue, 1)
