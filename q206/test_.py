from .code import Solution
from linked_list.base import SinglyLinkedList


def test_1():
    head = [1, 2, 3, 4, 5]
    res = [5, 4, 3, 2, 1]
    assert Solution().reverseList_local(SinglyLinkedList(head)).to_list() == res


def test_2():
    head = [1, 2]
    res = [2, 1]
    assert Solution().reverseList_local(SinglyLinkedList(head)).to_list() == res


def test_3():
    head = []
    res = []
    assert Solution().reverseList_local(SinglyLinkedList(head)).to_list() == res


def test_4():
    head = [1]
    res = [1]
    assert Solution().reverseList_local(SinglyLinkedList(head)).to_list() == res


"""
[1, 2, 3, 4, 5]
[1, 2]
[]
[1]
"""
