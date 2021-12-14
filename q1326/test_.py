from .code import Solution


def test_1():
    n = 5
    ranges = [3, 4, 1, 1, 0, 0]
    result = 1
    assert Solution().minTaps(n, ranges) == result


def test_2():
    n = 3
    ranges = [0, 0, 0, 0]
    result = -1
    assert Solution().minTaps(n, ranges) == result


def test_3():
    n = 7
    ranges = [1, 2, 1, 0, 2, 1, 0, 1]
    result = 3
    assert Solution().minTaps(n, ranges) == result


def test_4():
    n = 8
    ranges = [4, 0, 0, 0, 0, 0, 0, 0, 4]
    result = 2
    assert Solution().minTaps(n, ranges) == result


def test_5():
    n = 8
    ranges = [4, 0, 0, 0, 4, 0, 0, 0, 4]
    result = 1
    assert Solution().minTaps(n, ranges) == result


def test_6():
    n = 9
    ranges = [0, 5, 0, 3, 3, 3, 1, 4, 0, 4]
    result = 2
    assert Solution().minTaps(n, ranges) == result


def test_7():
    n = 35
    ranges = [1, 0, 4, 0, 4, 1, 4, 3, 1, 1, 1, 2, 1, 4, 0, 3, 0,
              3, 0, 3, 0, 5, 3, 0, 0, 1, 2, 1, 2, 4, 3, 0, 1, 0, 5, 2]
    result = 6
    assert Solution().minTaps(n, ranges) == result


def test_7():
    n = 5
    ranges = [3, 0, 1, 1, 0, 0]
    result = -1
    assert Solution().minTaps(n, ranges) == result


"""
5
[3,4,1,1,0,0]
3
[0, 0, 0, 0]
7
[1, 2, 1, 0, 2, 1, 0, 1]
8
[4, 0, 0, 0, 0, 0, 0, 0, 4]
8
[4, 0, 0, 0, 4, 0, 0, 0, 4]
9
[0,5,0,3,3,3,1,4,0,4]
35
[1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]
5
[3,0,1,1,0,0]
"""
