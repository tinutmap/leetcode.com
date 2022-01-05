from .code import Solution


def test_1():
    n = 2
    res = 2
    assert Solution().climbStairs(n) == res


def test_2():
    n = 3
    res = 3
    assert Solution().climbStairs(n) == res


def test_5():
    n = 5
    res = 8
    assert Solution().climbStairs(n) == res


"""
2
3
5
"""
