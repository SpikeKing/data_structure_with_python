#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29
"""
from Queue import Queue


def hot_potato(name_list, num):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.put(name)

    while sim_queue.qsize() > 1:
        for i in range(num - 1):
            item = sim_queue.get()
            sim_queue.put(item)
        p_name = sim_queue.get()
        # print('Dead: {}'.format(p_name))

    return sim_queue.get()


def test_of_hot_potato():
    name_list = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
    num = 3
    print(hot_potato(name_list, num))


if __name__ == '__main__':
    test_of_hot_potato()
