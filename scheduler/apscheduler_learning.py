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
import datetime
import os
import random
import threading
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def job(job_name):
    with open(job_name + ".log", 'a+') as f:
        f.write(
            'Start Time: {0}: job name-{1} thread_id-{2}, process_id-{3}'.format(
                str(datetime.datetime.now()),
                job_name,
                threading.get_ident(),
                os.getpid()
            )
        )
    num = random.randint(0, 1000)
    time.sleep(num)
    if num % 10 == 0:
        raise RuntimeError("random exception!")
    with open(job_name + ".log", 'a+') as f:
        f.write(
            'End Time: {0}: job name-{1} thread_id-{2}, process_id-{3}'.format(
                str(datetime.datetime.now()),
                job_name,
                threading.get_ident(),
                os.getpid()
            )
        )


if __name__ == '__main__':
    job_defaults = {'max_instances': 20}
    sched = BackgroundScheduler(timezone='UTC')
    for i in range(0, 10):
        job_name = "Job-{0}".format(i)
        sched.add_job(
            job,
            kwargs={
                "job_name": job_name
            },
            trigger=CronTrigger.from_crontab("*/5 * * * *"),
            name=job_name
        )
    sched.start()

    while True:
        # print(
        #     'main 1s: {0}'.format(round(time.time(), 3))
        # )
        time.sleep(1)
