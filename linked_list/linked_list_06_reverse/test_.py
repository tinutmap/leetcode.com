from ..base import SinglyLinkedList
from .code import Solution


def test_1():
    input = [1, 2, 3, 4, 5]
    result = [5, 4, 3, 2, 1]
    assert Solution().reverseList_local(SinglyLinkedList(input)) == result


def test_2():
    input = [1]
    result = [1]
    assert Solution().reverseList_local(SinglyLinkedList(input)) == result


def test_3():
    input = []
    result = []
    assert Solution().reverseList_local(SinglyLinkedList(input)) == result


'''
[1,2,3,4,5]
[1]
[]
'''
