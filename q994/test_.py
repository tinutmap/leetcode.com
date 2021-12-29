from .code import Solution


def test_1():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = 4
    assert Solution().orangesRotting(grid) == result


def test_2():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    result = -1
    assert Solution().orangesRotting(grid) == result


def test_3():
    grid = grid = [[0, 2]]
    result = 0
    assert Solution().orangesRotting(grid) == result


def test_4():
    grid = grid = [[1]]
    result = -1
    assert Solution().orangesRotting(grid) == result


def test_5():
    grid = grid = [[0]]
    result = 0
    assert Solution().orangesRotting(grid) == result


def test_6():
    grid = grid = [[2, 2]]
    result = 0
    assert Solution().orangesRotting(grid) == result


"""
[[2, 1, 1], [1, 1, 0], [0, 1, 1]]
[[2, 1, 1], [0, 1, 1], [1, 0, 1]]
[[0, 2]]
[[1]]
[[0]]
[[2, 2]]
"""
