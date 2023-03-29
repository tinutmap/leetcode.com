from .code import Solution


def test_1():
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    res = [1, -1, -1, -1, -1]
    assert Solution().findBall(grid) == res


def test_2():
    grid = [[-1]]
    res = [-1]
    assert Solution().findBall(grid) == res


def test_3():
    grid = [[1]]
    res = [-1]
    assert Solution().findBall(grid) == res


def test_4():
    grid = [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]
    res = [0, 1, 2, 3, 4, -1]
    assert Solution().findBall(grid) == res


"""
[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
[[-1]]
[[1]]
[[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
"""
