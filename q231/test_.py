from .code import Solution


def test_1():
    n = 1
    res = True
    assert Solution().isPowerOfTwo(n) == res


def test_2():
    n = 16
    res = True
    assert Solution().isPowerOfTwo(n) == res


def test_3():
    n = 3
    res = False
    assert Solution().isPowerOfTwo(n) == res


def test_4():
    n = 0
    res = False
    assert Solution().isPowerOfTwo(n) == res


def test_5():
    n = 2
    res = True
    assert Solution().isPowerOfTwo(n) == res


def test_6():
    n = -2
    res = False
    assert Solution().isPowerOfTwo(n) == res


"""
1
16
3
0
2
-2
"""
