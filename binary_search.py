#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/15

二分查找，时间复杂度O(logn)

排序一次，查找多次，排序成本可以忽略；
只查找一次，则顺序查找比较好。
"""


def binary_search(alist, item):
    """
    二分查找，非递归
    1. 2个参数，待查找alist和查找项item
    2. 声明3个变量，first，last，found(返回值)
    3. while条件，first小于等于last，found是false
    4. mid是first和last的中值(整除)；
    5. 三个if条件，相等alist[mid]=item，小于中值换last，大于中值换first；
    6. 返回found，13行
    :param alist: 待查找alist
    :param item: 待查找项item
    :return: 是否找到
    """
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def binary_search_re(alist, item):
    """
    二分查找，递归
    1. if终止条件，长度为0，返回False；
    2. 中点是长度除2，中值判断；
    3. 小于递归前半部分，大于递归后半部分，返回递归函数；
    4. 11行
    :param alist: 待查找alist
    :param item: 待查找项item
    :return: 是否找到
    """
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binary_search_re(alist[:mid], item)
            else:
                return binary_search_re(alist[mid + 1:], item)


def test_of_binary_search():
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(test_list, 3))
    print(binary_search(test_list, 13))
    print(binary_search_re(test_list, 3))
    print(binary_search_re(test_list, 13))


if __name__ == '__main__':
    test_of_binary_search()
