#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/15

冒泡排序，时间复杂度O(n^2)

冒泡排序通常被认为是低效的排序方式。
优势是：识别排序列表，和提前终止排序
"""


def bubble_sort(alist):
    """
    冒泡排序
    1. 两次遍历，第1次遍历长度，倒序逐渐减1，每遍历一次，排序一个；
    2. 第2次，正常遍历，少1个值，因为i和i+1；
    3. 当前位大于下一位，交换当前位和下一位；
    4. 4行
    :param alist: 待排序列表
    :return: None，内部排序
    """
    for p_num in range(len(alist) - 1, 0, -1):
        for i in range(p_num):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def short_bubble_sort(alist):
    """
    短冒泡排序，增加exchange，额外终止参数
    1. 初始为True，当为False时终止；
    2. 在第2次循环前，设置为False，交换一次就设置为True，一次未交换则触发终止；
    3. 9行，增加5行的exchange操作
    :param alist:
    :return:
    """
    exchange = True
    for p_num in range(len(alist) - 1, 0, -1):
        if not exchange:
            break
        exchange = False
        for i in range(p_num):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchange = True


def test_of_bubble_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # bubble_sort(alist)
    # print(alist)
    alist = [17, 20, 26, 93, 77, 31, 44, 55, 54]
    short_bubble_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_bubble_sort()
