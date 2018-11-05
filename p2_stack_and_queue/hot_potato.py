#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29
"""
from queue import Queue


def hot_potato(name_list, num):
    """
    烫手的山芋，循环去除
    :param name_list: 名字列表
    :param num: 循环数
    :return: 最后剩下的人
    """
    q = Queue()

    for name in name_list:
        q.put(name)

    while q.qsize() > 1:
        for i in range(num - 1):  # 每次都死一个循环，最后一个死亡
            live = q.get()
            q.put(live)
        dead = q.get()  # 输出死亡
        print('Dead: {}'.format(dead))

    return q.get()


def test_of_hot_potato():
    name_list = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
    num = 3
    print(hot_potato(name_list, num))


if __name__ == '__main__':
    test_of_hot_potato()
