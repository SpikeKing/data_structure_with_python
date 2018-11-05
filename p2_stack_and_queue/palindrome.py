#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29

回文，deque
"""
from collections import deque


def pal_checker(a_str):
    """
    回文，双端队列
    :param a_str: 输入字符串
    :return: 是否回文
    """
    q_char = deque()

    for ch in a_str:
        q_char.append(ch)

    still_equal = True

    # while的终止条件长度或者Bool
    while len(q_char) > 1 and still_equal:
        first = q_char.pop()
        last = q_char.popleft()
        if first != last:
            still_equal = False

    return still_equal


def test_of_pal_checker():
    print(pal_checker('lsdkjfskf'))
    print(pal_checker('radar'))


if __name__ == '__main__':
    test_of_pal_checker()
