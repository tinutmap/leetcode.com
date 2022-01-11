from .code import Solution


def test_1():
    numRows = 5
    res = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert Solution().generate(numRows) == res


def test_2():
    numRows = 1
    res = [[1]]
    assert Solution().generate(numRows) == res


def test_3():
    numRows = 2
    res = [[1], [1, 1]]
    assert Solution().generate(numRows) == res


def test_4():
    numRows = 6
    res = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
           [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert Solution().generate(numRows) == res


"""
5
1
2
6
"""
