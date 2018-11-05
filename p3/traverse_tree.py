#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/31
"""


class TreeClz(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def traverse_order(tree_head):
    """
    遍历二叉树
    前序: 0134256
    中序: 3140526
    后序: 3415620
    :param tree_head: 树的头结点
    :return: None
    """
    if not tree_head:
        return
    # print(tree_head.data, end='')  # 前序遍历
    traverse_order(tree_head.left)
    # print(tree_head.data, end='')  # 中序遍历
    traverse_order(tree_head.right)
    # print(tree_head.data, end='')  # 后序遍历


def init_tree():
    """
    初始化二叉数
       0
     1   2
    3 4 5 6
    :return: 二叉树的根节点
    """
    root = TreeClz(0)
    node1 = TreeClz(1)
    node2 = TreeClz(2)
    node3 = TreeClz(3)
    node4 = TreeClz(4)
    node5 = TreeClz(5)
    node6 = TreeClz(6)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    return root


def test_tree():
    tree_head = init_tree()
    traverse_order(tree_head)


if __name__ == '__main__':
    test_tree()
