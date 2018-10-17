#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/16

归并排序，时间复杂度O(nlogn)，合并过程需要额外的空间，左右两个部分。
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
    left = alist[:mid]
    right = alist[mid:]
    merge_sort(left)
    merge_sort(right)
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k += 1
    if i < len(left):
        alist[k:] = left[i:]
    if j < len(right):
        alist[k:] = right[j:]


def test_of_merge_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_merge_sort()
