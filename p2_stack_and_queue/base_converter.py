#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29
"""


def base_converter(num, base):
    """
    将二进制转换为其他进制
    :param num: 数字
    :param base: 基数
    :return: 数字的字符串
    """
    digs = '0123456789ABCDEF'  # 支持16位
    base_stack = list()

    while num > 0:
        rem = num % base
        base_stack.append(rem)
        num //= base  # 递减一直到0

    res_str = ''  # 转换为str
    while base_stack:
        res_str += digs[base_stack.pop()]

    return res_str


if __name__ == '__main__':
    print(base_converter(25, 2))
    print(base_converter(25, 16))
