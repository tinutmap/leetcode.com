from .code import Solution
from ..base import SinglyLinkedList


def test_1():
    head = [1, 2, 2, 1]
    result = True
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_2():
    head = [1, 2]
    result = False
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


# def test_3():
#     head = []
#     result = True
#     assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_4():
    head = [1]
    result = True
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_5():
    head = [1, 2, 3, 2, 1]
    result = True
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_6():
    head = [1, 2, 1]
    result = True
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_7():
    head = [1, 3, 2, 4, 3, 2, 1]
    result = False
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_8():
    head = [1, 0, 0]
    result = False
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_9():
    head = [8, 0, 7, 1, 7, 7, 9, 7, 5, 2, 9, 1, 7, 3, 7, 0, 6, 5, 1, 7, 7, 9, 3, 8, 1, 5, 7, 7, 8, 4, 0, 9, 3, 7, 3, 4, 5, 7, 4, 8, 8, 5,
            8, 9, 8, 5, 8, 8, 4, 7, 5, 4, 3, 7, 3, 9, 0, 4, 8, 7, 7, 5, 1, 8, 3, 9, 7, 7, 1, 5, 6, 0, 7, 3, 7, 1, 9, 2, 5, 7, 9, 7, 7, 1, 7, 0, 8]
    result = True
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


def test_10():
    head = [1, 2, 3, 3, 2, 1]
    result = True
    assert(Solution().isPalindrome_local(SinglyLinkedList(head))) == result


'''
[1,2,2,1]
[1, 2]
[1]
[1,2,3,2,1]
[1,2,1]
[1,3,2,4,3,2,1]
[1,0,0]
[1, 2, 3, 3, 2, 1]
[8, 0, 7, 1, 7, 7, 9, 7, 5, 2, 9, 1, 7, 3, 7, 0, 6, 5, 1, 7, 7, 9, 3, 8, 1, 5, 7, 7, 8, 4, 0, 9, 3, 7, 3, 4, 5, 7, 4, 8, 8, 5, 8, 9, 8, 5, 8, 8, 4, 7, 5, 4, 3, 7, 3, 9, 0, 4, 8, 7, 7, 5, 1, 8, 3, 9, 7, 7, 1, 5, 6, 0, 7, 3, 7, 1, 9, 2, 5, 7, 9, 7, 7, 1, 7, 0, 8]
'''
