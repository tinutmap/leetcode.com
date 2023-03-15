from .code import Solution


def test_1():
    n = 0
    res = 0
    assert Solution().fib(n) == res


def test_2():
    n = 1
    res = 1
    assert Solution().fib(n) == res


def test_3():
    n = 5
    res = 5
    assert Solution().fib(n) == res


def test_4():
    n = 14
    res = 377
    assert Solution().fib(n) == res


"""
2
3
4
5
14
"""
