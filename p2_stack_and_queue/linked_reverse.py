#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/10/29
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


def reverse_list(node_head):
    """
    链表逆序，交换链表
    :param node_head: 链表头
    :return: 新的链表的头结点
    """
    prev_node = None

    while node_head:
        next_node = node_head.next_node
        node_head.next_node = prev_node
        prev_node = node_head
        node_head = next_node

    return prev_node


def init_list():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next_node = n2
    n2.next_node = n3
    n3.next_node = n4
    n4.next_node = n5
    return n1


def show_list(node_head):
    head = node_head
    while head:
        print(head.data, end=' ')
        head = head.next_node


def test_of_reverse_list():
    head_node = init_list()
    show_list(head_node)
    print()
    head_node = reverse_list(head_node)
    show_list(head_node)


if __name__ == '__main__':
    test_of_reverse_list()
