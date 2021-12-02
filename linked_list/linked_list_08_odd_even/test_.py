from .code import Solution
from ..base import SinglyLinkedList


def test_1():
    head = [1, 2, 3, 4, 5]
    result = [1, 3, 5, 2, 4]
    assert Solution().oddEvenList_local(SinglyLinkedList(head)) == result


def test_2():
    head = [1, 2]
    result = [1, 2]
    assert Solution().oddEvenList_local(SinglyLinkedList(head)) == result


def test_3():
    head = [1]
    result = [1]
    assert Solution().oddEvenList_local(SinglyLinkedList(head)) == result


def test_4():
    head = []
    result = []
    assert Solution().oddEvenList_local(SinglyLinkedList(head)) == result


def test_5():
    head = [2, 1, 3, 5, 6, 4, 7]
    result = [2, 3, 6, 7, 1, 5, 4]
    assert Solution().oddEvenList_local(SinglyLinkedList(head)) == result

'''
[1,2,3,4,5]
[1,2]
[1]
[]
[2, 1, 3, 5, 6, 4, 7]
'''