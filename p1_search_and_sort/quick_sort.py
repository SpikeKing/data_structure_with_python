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
    1. 确定终止条件，起始大于等于终止；
    2. 起始fst和终止lst的位置，枢轴值pivot是第1个值；
    3. 遍历i和j，i是第2个，j是最后一个；
    4. 循环交换，直到i和j交叉；
    5. 枢轴索引取i和j最小的1个；
    6. 交换枢轴位置的值与起始位置的值；
    7. 递归调用左右两部分；
    8. 16行
    :param alist: 待排序列表
    :param fst: 起始idx
    :param lst: 终止idx
    :return: None
    """
    if fst >= lst:
        return
    pivot = alist[fst]
    i, j = fst + 1, lst
    while i <= j:  # 增加等号，用于移动中心轴位置，最后交换使用
        while alist[i] < pivot:
            i += 1
        while alist[j] > pivot:
            j -= 1
        if i < j:
            alist[i], alist[j] = alist[j], alist[i]
            i, j = i + 1, j - 1
    p_idx = min(i, j)  # 枢轴索引
    alist[fst], alist[p_idx] = alist[p_idx], alist[fst]
    quick_sort(alist, fst, p_idx - 1)
    quick_sort(alist, p_idx + 1, lst)


def quick_sort_v2(alist):
    """
    快速排序，需要额外空间
    :param alist: 待排序列表
    :return: 排序列表
    """
    if len(alist) <= 1:
        return alist
    pivot = alist[0]
    small = [i for i in alist if i < pivot]
    mid = [i for i in alist if i == pivot]
    large = [i for i in alist if i > pivot]
    return quick_sort_v2(small) + mid + quick_sort_v2(large)


def test_of_quick_sort():
    # alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    alist = [54, 26, 93, 17, 77, 56, 26, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
    # alist = quick_sort_v2(alist)
    # print(alist)


if __name__ == '__main__':
    test_of_quick_sort()
