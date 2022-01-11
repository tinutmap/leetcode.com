from .code import Solution


def test_1():
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    res = [[1, 2, 3, 4]]
    assert Solution().matrixReshape(mat, r, c) == res


def test_2():
    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4
    res = [[1, 2], [3, 4]]
    assert Solution().matrixReshape(mat, r, c) == res


def test_3():
    mat = [[1, 2], [3, 4], [5, 6], [7, 8]]
    r = 2
    c = 4
    res = [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert Solution().matrixReshape(mat, r, c) == res


def test_4():
    mat = [[1]]
    r = 1
    c = 1
    res = [[1]]
    assert Solution().matrixReshape(mat, r, c) == res


"""
[[1,2],[3,4]]
1
4
[[1,2],[3,4]]
2
4
[[1, 2], [3, 4], [5, 6], [7, 8]]
2
4
[[1]]
1
1
"""
