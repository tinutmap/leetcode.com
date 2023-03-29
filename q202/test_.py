from .code import Solution


def test_1():
    n = 19
    res = True
    assert Solution().isHappy(n) == res


def test_2():
    n = 2
    res = False
    assert Solution().isHappy(n) == res


def test_3():
    n = 7
    res = True
    assert Solution().isHappy(n) == res


def test_4():
    n = 78
    res = False
    assert Solution().isHappy(n) == res


"""
19
2
7
78
"""
