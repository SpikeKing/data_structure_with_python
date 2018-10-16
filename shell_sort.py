#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/15

希尔排序，时间复杂度，介于O(n)~O(n^2)，也可以认为是O(n^3/2)
插入排序的改进，比较和移位较少，每次遍历都会生成一个"更有序"的子列表
"""


def shell_sort(alist):
    """
    希尔排序
    1. 两部分，第1部分，计算增量gap和起始位置s_pos；
    2. 增量是累除2，s_pos是增量的遍历
    3. 增量插入排序，额外传入起始位置和增量；
    4. range的起始由起始位置+增量；
    5. 循环条件为大于等于增量，差值为增量
    6. 12行，增量部分5行，插入部分7行
    :param alist: 待排序alist
    :return: None
    """
    gap = len(alist) // 2
    while gap > 0:
        for s_pos in range(gap):
            gap_insert_sort(alist, s_pos, gap)
        gap = gap // 2


def gap_insert_sort(alist, s_pos, gap):
    """
    带增量的插入排序
    :param alist: 待排序alist
    :param s_pos: 起始位置
    :param gap: 增量
    :return: None
    """
    for idx in range(s_pos + gap, len(alist), gap):
        cur_val = alist[idx]
        pos = idx
        while pos >= gap and alist[pos - gap] > cur_val:
            alist[pos] = alist[pos - gap]
            pos -= gap
        alist[pos] = cur_val


def test_of_shell_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_shell_sort()
