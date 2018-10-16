#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/16

快速排序，时间复杂度O(nlogn)，不需要额外空间。
"""


def quick_sort(alist, fst, lst):
    """
    快速排序
    1. 确定终止条件，起始等于终止；
    2. 起始fst和终止lst的位置，枢轴的值pivot；
    3. 遍历i和j；
    4. 14行
    :param alist: 待排序列表
    :param fst: 起始idx
    :param lst: 终止idx
    :return: None
    """
    if fst >= lst:
        return
    i, j = fst, lst
    pivot = alist[fst]
    while i <= j:
        while alist[i] < pivot:
            i += 1
        while alist[j] > pivot:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i, j = i + 1, j - 1
    quick_sort(alist, fst, j)
    quick_sort(alist, i, lst)


def quick_sort_v2(alist):
    """
    快速排序
    :param alist:
    :return:
    """
    if len(alist) < 2:
        return alist
    pivot = alist[0]
    small = [i for i in alist if i < pivot]
    medium = [i for i in alist if i == pivot]
    large = [i for i in alist if i > pivot]
    return quick_sort_v2(small) + medium + quick_sort_v2(large)


def test_of_quick_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # quick_sort(alist, 0, len(alist) - 1)
    # print(alist)
    alist = quick_sort_v2(alist)
    print(alist)


if __name__ == '__main__':
    test_of_quick_sort()
