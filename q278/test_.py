from .q278 import Solution


def test_1():
    n = 5
    res = 4
    assert Solution(res).firstBadVersion(n) == res


def test_2():
    n = 1
    res = 1
    assert Solution(res).firstBadVersion(n) == res


def test_3():
    n = 2
    res = 2
    assert Solution(res).firstBadVersion(n) == res
