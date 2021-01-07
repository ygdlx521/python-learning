#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author  :   daliang
@Contact :   yunlianghe@appannie.com
@Software:   PyCharm
@File    :   split_csv.py
@Create  :   2020/12/24 7:56 PM
@License :   (C) Copyright 2019-2020, App Annie Inc.
@Desc    :
"""

# encoding=utf-8
import os
import time


# 2019/9/8 将大的csv文件拆分多个小的csv文件

def mkSubFile(lines, head, srcName, sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    fout = open(filename, 'w')
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()


def splitByLineCount(filename, count):
    fin = open(filename, encoding="utf-8")
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filename, sub)
    finally:
        fin.close()


if __name__ == '__main__':
    begin = time.time()
    splitByLineCount('123231211.csv', 200000)  # 每个小的csv文件存放1000条
    end = time.time()
    print('time is %d seconds ' % (end - begin))
