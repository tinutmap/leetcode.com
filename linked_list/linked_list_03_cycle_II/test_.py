# from .code import Head, Solution, ListNode
from .code import Head, Solution, ListNode


def test_1():
    pos = 1
    l = [3, 2, 0, -4]
    data = Head(l, pos)
    assert print(Solution().detectCycle_local(data)) == print(ListNode(l[pos]))


def test_2():
    pos = 0
    l = [1, 2]
    data = Head(l, pos)
    assert print(Solution().detectCycle_local(data)) == print(ListNode(l[pos]))


def test_3():
    pos = -1
    l = [1]
    data = Head(l, pos)
    assert print(Solution().detectCycle_local(data)) == print(ListNode(l[pos]))


def test_4():
    pos = 0
    l = [1]
    data = Head(l, pos)
    assert print(Solution().detectCycle_local(data)) == print(ListNode(l[pos]))
