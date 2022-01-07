from .code import Solution


def test_1():
    n = 11
    res = 3489660928
    assert Solution().reverseBits(n) == res


def test_2():
    n = 10
    res = 1342177280
    assert Solution().reverseBits(n) == res


def test_3():
    n = 0
    res = 0
    assert Solution().reverseBits(n) == res


def test_4():
    n = 43261596
    res = 964176192
    assert Solution().reverseBits(n) == res


def test_5():
    n = 4294967293
    res = 3221225471
    assert Solution().reverseBits(n) == res


"""
11
10
0
43261596
4294967293
"""
