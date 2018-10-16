#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/15

插入排序，时间复杂度O(n^2)
用移位代替交换，移位操作的时间大约是交换时间的1/3。
"""


def insert_sort(alist):
    """
    插入排序，
    1. 遍历列表，存储当前值cur_val，设置游标pos
    2. 游标大于0和游标的值大于当前值，则移位，同时游标减1；
    3. 将当前值赋予游标的终止位置；
    4. 7行
    :param alist: 待排序alist
    :return: None
    """
    for idx in range(1, len(alist)):
        cur_val = alist[idx]
        pos = idx  # 游标
        while pos > 0 and alist[pos - 1] > cur_val:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = cur_val  # 最后游标的位置


def test_of_insert_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_insert_sort()
