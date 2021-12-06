from .code import Solution
from linked_list.base import SinglyLinkedList


def test_1():
    head = [1, 2, 3, 4, 5]
    result = [3, 4, 5]
    assert Solution().middleNode_local(SinglyLinkedList(head)) == result


def test_2():
    head = [1, 2, 3, 4, 5, 6]
    result = [4, 5, 6]
    assert Solution().middleNode_local(SinglyLinkedList(head)) == result


def test_3():
    head = [1]
    result = [1]
    assert Solution().middleNode_local(SinglyLinkedList(head)) == result


def test_4():
    head = [1, 2]
    result = [2]
    assert Solution().middleNode_local(SinglyLinkedList(head)) == result


def test_5():
    head = [1, 2, 3]
    result = [2, 3]
    assert Solution().middleNode_local(SinglyLinkedList(head)) == result


def test_6():
    head = [1, 2, 3, 4]
    result = [3, 4]
    assert Solution().middleNode_local(SinglyLinkedList(head)) == result


'''
[1,2,3,4,5]
[1, 2, 3, 4, 5, 6]
[1]
[1,2]
[1, 2, 3]
[1, 2, 3, 4]
'''
