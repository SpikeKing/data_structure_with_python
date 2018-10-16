#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/16

归并排序，时间复杂度O(nlogn)，合并过程需要额外的空间。
"""


def merge_sort(alist):
    """
    归并排序
    1. 递归，结束条件，只有1个元素，return；
    2. mid中心，左右两部分，递归调用merge_sort；
    3. 遍历左右，添加较小的值；遍历其余部分；
    4. 20行
    :param alist:
    :return:
    """
    if len(alist) < 2:
        return
    mid = len(alist) // 2
    left_half = alist[:mid]
    right_half = alist[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    i, j, k = 0, 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            alist[k] = left_half[i]
            i += 1
        else:
            alist[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        alist[k:] = left_half[i:]
    while j < len(right_half):
        alist[k:] = right_half[i:]


def test_of_merge_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_merge_sort()
