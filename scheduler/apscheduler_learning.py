#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author  :   daliang
@Contact :   yunlianghe@appannie.com
@Software:   PyCharm
@File    :   apscheduler_learning.py
@Create  :   2020/11/13 5:31 PM
@License :   (C) Copyright 2019-2020, App Annie Inc.
@Desc    :
"""

import os
import threading
import time

from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print(
        'Time: {0}: job thread_id-{1}, process_id-{2}'.format(
            round(time.time(), 3),
            threading.get_ident(),
            os.getpid()
        )
    )
    time.sleep(5)


if __name__ == '__main__':
    job_defaults = {'max_instances': 20}
    sched = BackgroundScheduler(timezone='UTC')
    for i in range(0, 10):
        job_name = "Job-{0}".format(i)
        sched.add_job(job, 'interval', seconds=10, name=job_name)
    sched.start()

    while True:
        print(
            'main 1s: {0}'.format(round(time.time(), 3))
        )
        time.sleep(1)


