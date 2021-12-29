from .code import Solution
from linked_list.base import SinglyLinkedList


def test_1():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    result = [1, 1, 2, 3, 4, 4]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_2():
    list1 = []
    list2 = []
    result = []
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_3_1():
    list1 = []
    list2 = [0]
    result = [0]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_3_2():
    list1 = [0]
    list2 = []
    result = [0]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_4():
    list1 = [1, 2, 4, 5]
    list2 = [1, 3, 4]
    result = [1, 1, 2, 3, 4, 4, 5]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_5():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4, 5]
    result = [1, 1, 2, 3, 4, 4, 5]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_6():
    list1 = [1]
    list2 = [1, 3, 4, 5]
    result = [1, 1, 3, 4, 5]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_7():
    list1 = [1, 3, 4, 5]
    list2 = [1]
    result = [1, 1, 3, 4, 5]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


def test_8():
    list1 = [2]
    list2 = [1]
    result = [1, 2]
    assert Solution().mergeTwoLists_local(SinglyLinkedList(list1),
                                          SinglyLinkedList(list2)).to_list() == result


"""
[1,2,4]
[1,3,4]
[]
[]
[]
[0]
[0]
[]
[1, 2, 4, 5]
[1, 3, 4]
[1, 2, 4]
[1, 3, 4, 5]
[1]
[1, 3, 4, 5]
[1, 3, 4, 5]
[1]
[2]
[1]
"""
