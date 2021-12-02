from .code import LinkedList, Solution, ListNode


def test_1():
    head = [1, 2, 3, 4, 5]
    n = 2
    result = [1, 2, 3, 5]
    assert Solution().removeNthFromEnd_local(
        LinkedList(head), n) == result


def test_2():
    head = [1]
    n = 1
    result = []
    assert Solution().removeNthFromEnd_local(
        LinkedList(head), n) == result


def test_3():
    head = [1, 2]
    n = 1
    result = [1]
    assert Solution().removeNthFromEnd_local(
        LinkedList(head), n) == result


def test_4():
    head = [1, 2]
    n = 2
    result = [2]
    assert Solution().removeNthFromEnd_local(
        LinkedList(head), n) == result


'''
# Leetcode test input
[1,2,3,4,5]
2
[1]
1
[1, 2]
1
[1, 2]
2
'''
