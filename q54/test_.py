from .code import Solution


def test_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert Solution().spiralOrder(matrix) == res


def test_2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    res = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert Solution().spiralOrder(matrix) == res


"""
"""
