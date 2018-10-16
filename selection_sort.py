#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/15

选择排序，时间复杂度O(n^2)
比较次数与冒泡排序相同，交换次数小于冒泡排序。
"""


def selection_sort(alist):
    """
    选择排序，即选择最大值再交换
    1. 依然是2次遍历，第1次反序，第2次正序，注意起始为1，末尾+1；
    2. max_loc存储最大值，默认第0位；
    3. 当loc的值大于max_loc的值时，max_loc重新赋值；
    4. 交换loc和max_loc
    5. 6行
    :param alist: 待排序alist
    :return: None
    """
    for p_num in range(len(alist) - 1, 0, -1):
        max_loc = 0
        for loc in range(1, p_num + 1):
            if alist[loc] > alist[max_loc]:
                max_loc = loc
        alist[p_num], alist[max_loc] = alist[max_loc], alist[p_num]


def tes_of_selection_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(alist)
    print(alist)


if __name__ == '__main__':
    tes_of_selection_sort()
