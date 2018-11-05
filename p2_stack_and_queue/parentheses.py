#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29
"""


def par_checker(symbol_str):
    """
    括号匹配，list包含栈的功能
    append是添加，pop是删除
    https://docs.python.org/2/tutorial/datastructures.html
    14行
    :param symbol_str: 符号字符串
    :return: 是否
    """
    s = list()  # python的list可以实现stack功能
    idx = 0
    while idx < len(symbol_str):
        symbol = symbol_str[idx]
        if symbol == '(':
            s.append(symbol)
        elif symbol == ')':
            s.pop()
        idx += 1
    if not s:
        return True
    else:
        return False


def test_of_par_checker():
    print(par_checker('(())'))
    print(par_checker('((()'))
    print(par_checker('(a)()((()))'))


if __name__ == '__main__':
    test_of_par_checker()
