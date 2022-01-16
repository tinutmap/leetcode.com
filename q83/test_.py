from .code import Solution
from linked_list.base import SinglyLinkedList


def test_1():
    head = [1, 1, 2]
    res = [1, 2]
    assert Solution().deleteDuplicates_local(
        SinglyLinkedList(head)).to_list() == res


def test_2():
    head = [1, 1, 2, 3, 3]
    res = [1, 2, 3]
    assert Solution().deleteDuplicates_local(
        SinglyLinkedList(head)).to_list() == res


def test_3():
    head = [1]
    res = [1]
    assert Solution().deleteDuplicates_local(
        SinglyLinkedList(head)).to_list() == res


def test_4():
    head = []
    res = []
    assert Solution().deleteDuplicates_local(
        SinglyLinkedList(head)).to_list() == res


"""
[1, 1, 2]
[1, 1, 2, 3, 3]
[1]
[1, 1, 2, 3, 3]
[]
[1,2,3,3,3]
"""
