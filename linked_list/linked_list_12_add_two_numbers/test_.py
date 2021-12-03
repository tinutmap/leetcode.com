from ..base import ListNode, SinglyLinkedList
from .code import Solution


def test_1():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    result = [7, 0, 8]
    assert Solution().addTwoNumbers_local(
        SinglyLinkedList(l1), SinglyLinkedList(l2)) == result


def test_2():
    l1 = [0]
    l2 = [0]
    result = [0]
    assert Solution().addTwoNumbers_local(
        SinglyLinkedList(l1), SinglyLinkedList(l2)) == result


def test_3():
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    result = [8, 9, 9, 9, 0, 0, 0, 1]
    assert Solution().addTwoNumbers_local(
        SinglyLinkedList(l1), SinglyLinkedList(l2)) == result


def test_4():
    l1 = [2, 4, 3, 9]
    l2 = [5, 6, 6]
    result = [7, 0, 0, 0, 1]
    assert Solution().addTwoNumbers_local(
        SinglyLinkedList(l1), SinglyLinkedList(l2)) == result


def test_5():
    l1 = [2, 4, 3]
    l2 = [5, 6, 6, 9]
    result = [7, 0, 0, 0, 1]
    assert Solution().addTwoNumbers_local(
        SinglyLinkedList(l1), SinglyLinkedList(l2)) == result


def test_6():
    l1 = [5]
    l2 = [5]
    result = [0, 1]
    assert Solution().addTwoNumbers_local(
        SinglyLinkedList(l1), SinglyLinkedList(l2)) == result


def test_7():
    l1 = [9, 9, 9, 9, 9, 9, 9, 0, 1]
    l2 = [9, 9, 9, 9]
    result = [8, 9, 9, 9, 0, 0, 0, 1, 1]
    assert Solution().addTwoNumbers_local(
        SinglyLinkedList(l1), SinglyLinkedList(l2)) == result


'''
[2,4,3]
[5,6,4]
[0]
[0]
[9, 9, 9, 9, 9, 9, 9]
[9, 9, 9, 9]
[2, 4, 3, 9]
[5, 6, 6]
[2, 4, 3]
[5, 6, 6, 9]
[5]
[5]
[9, 9, 9, 9, 9, 9, 9, 0, 1]
[9, 9, 9, 9]
'''
