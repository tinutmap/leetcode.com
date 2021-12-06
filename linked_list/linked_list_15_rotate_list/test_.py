from .code import Solution
from ..base import SinglyLinkedList


def test_1():
    head = [1, 2, 3, 4, 5]
    k = 2
    result = [4, 5, 1, 2, 3]
    assert Solution().rotateRight_local(SinglyLinkedList(head), k) == result


def test_2():
    head = [1]
    k = 2
    result = [1]
    assert Solution().rotateRight_local(SinglyLinkedList(head), k) == result


def test_3():
    head = []
    k = 1
    result = []
    assert Solution().rotateRight_local(SinglyLinkedList(head), k) == result


def test_4():
    head = [1, 2, 3]
    k = 4
    result = [3, 1, 2]
    assert Solution().rotateRight_local(SinglyLinkedList(head), k) == result


def test_5():
    head = [1, 2, 3]
    k = 3
    result = [1, 2, 3]
    assert Solution().rotateRight_local(SinglyLinkedList(head), k) == result


'''
[1,2,3,4,5]
2
[1]
2
[]
1
[1,2,3]
4
[1,2,3]
3
'''
