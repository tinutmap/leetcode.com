from .code import Solution


def test_1():
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    res = 11
    assert Solution().minimumTotal(triangle) == res


def test_2():
    triangle = [[-10]]
    res = -10
    assert Solution().minimumTotal(triangle) == res


"""
[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
[[-10]]
"""
