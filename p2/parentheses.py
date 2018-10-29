#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29
"""


def par_checker(symbol_str):
    s = list()  # python的list可以实现stack功能
    balanced = True
    idx = 0
    while idx < len(symbol_str) and balanced:
        symbol = symbol_str[idx]
        if symbol == '(':
            s.append(symbol)
        else:
            if not symbol:
                balanced = False
            else:
                s.pop()
        idx += 1

    if balanced and not s:
        return True
    else:
        return False


def test_of_par_checker():
    print(par_checker('((()'))
    print(par_checker('()()((()))'))


if __name__ == '__main__':
    test_of_par_checker()
