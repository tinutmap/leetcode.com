from .code import Solution


def test_1():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    res = True
    assert Solution().searchMatrix(matrix, target) == res


def test_2():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    res = False
    assert Solution().searchMatrix(matrix, target) == res


def test_3():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20],
              [23, 30, 34, 60], [61, 62, 63, 64]]
    target = 60
    res = True
    assert Solution().searchMatrix(matrix, target) == res


def test_4():
    matrix = [[1, 3, 5, 7, 9], [10, 11, 16, 20, 21],
              [23, 30, 34, 60, 61], [63, 64, 65, 66, 67]]
    target = 66
    res = True
    assert Solution().searchMatrix(matrix, target) == res


def test_4():
    matrix = [[1]]
    target = 1
    res = True
    assert Solution().searchMatrix(matrix, target) == res


"""
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
3
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
13
[[1, 3, 5, 7], [10, 11, 16, 20],[23, 30, 34, 60], [61, 62, 63, 64]]
60
[[1, 3, 5, 7, 9], [10, 11, 16, 20, 21],[23, 30, 34, 60, 61], [63, 64, 65, 66, 67]]
66
[[1]]
1
"""
