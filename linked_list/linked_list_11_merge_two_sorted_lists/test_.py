from ..base import SinglyLinkedList
from .code import Solution


def test_1():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    result = [1, 1, 2, 3, 4, 4]
    assert Solution().mergeTwoLists_local(
        SinglyLinkedList(list1), SinglyLinkedList(list2)) == result


def test_2():
    list1 = []
    list2 = []
    result = []
    assert Solution().mergeTwoLists_local(
        SinglyLinkedList(list1), SinglyLinkedList(list2)) == result


def test_3():
    list1 = []
    list2 = [0]
    result = [0]
    assert Solution().mergeTwoLists_local(
        SinglyLinkedList(list1), SinglyLinkedList(list2)) == result


def test_4():
    list1 = [0]
    list2 = []
    result = [0]
    assert Solution().mergeTwoLists_local(
        SinglyLinkedList(list1), SinglyLinkedList(list2)) == result


def test_5():
    list1 = [1, 2, 4]
    list2 = [1, 3, 3]
    result = [1, 1, 2, 3, 3, 4]
    assert Solution().mergeTwoLists_local(
        SinglyLinkedList(list1), SinglyLinkedList(list2)) == result


'''
[1,2,4]
[1,3,4]
[]
[]
[]
[0]
[0]
[]
[1, 2, 4]
[1, 3, 3]
'''
