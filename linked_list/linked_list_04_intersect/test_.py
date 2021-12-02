'''
# Test for Failed Solution
from .code import Solution, LinkedList, ListNode


def test_1():
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    result = ListNode(8)
    assert Solution().getIntersectionNode_local(
        LinkedList(listA, result), LinkedList(listB, result)) == result


def test_2():
    listA = [1, 9, 1, 2, 4]
    listB = [3, 2, 4]
    result = ListNode(2)
    assert Solution().getIntersectionNode_local(
        LinkedList(listA, result), LinkedList(listB, result)) == result


def test_3():
    listA = [2, 6, 4]
    listB = [1, 5]
    result = ListNode(0)
    assert Solution().getIntersectionNode_local(
        LinkedList(listA, result), LinkedList(listB, result)) == result.val

'''

'''
# leetcode test input

8
[4,1,8,4,5]
[5,6,1,8,4,5]
2
3
0
[2,6,4]
[1,5]
3
2
2
[1,9,1,2,4]
[3,2,4]
3
1
'''
