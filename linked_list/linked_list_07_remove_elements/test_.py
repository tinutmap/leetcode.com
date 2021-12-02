from .code import Solution
from ..base import ListNode, SinglyLinkedList


def test_1():
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    result = [1, 2, 3, 4, 5]
    assert Solution().removeElements_local(SinglyLinkedList(head), val) == result


def test_2():
    head = []
    val = 1
    result = []
    assert Solution().removeElements_local(SinglyLinkedList(head), val) == result


def test_3():
    head = [7, 7, 7, 7]
    val = 7
    result = []
    assert Solution().removeElements_local(SinglyLinkedList(head), val) == result


'''
[1,2,6,3,4,5,6]
6
[]
1
[7,7,7,7]
7
'''
