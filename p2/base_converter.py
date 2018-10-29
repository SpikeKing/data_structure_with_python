#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29
"""


def base_converter(dec_num, base):
    """
    将2进制转换为其他进制
    :param dec_num: 数字
    :param base: 基数
    :return: 数字的字符串
    """
    digists = '0123456789ABCDEF'  # 支持16位
    rem_stack = list()

    while dec_num > 0:
        rem = dec_num % base
        rem_stack.append(rem)
        dec_num //= base  # 递减一直到0

    new_str = ''  # 转换为str
    while rem_stack:
        new_str += digists[rem_stack.pop()]

    return new_str


if __name__ == '__main__':
    print(base_converter(25, 2))
    print(base_converter(25, 16))
