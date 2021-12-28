from .code import Solution


def test_1():
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().updateMatrix(mat) == result


def test_2():
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert Solution().updateMatrix(mat) == result


def test_3():
    mat = [[0], [0], [0], [0], [0]]
    result = [[0], [0], [0], [0], [0]]
    assert Solution().updateMatrix(mat) == result


def test_4():
    mat = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    result = [
        [19, 19, 19],
        [18, 18, 18],
        [17, 17, 17],
        [16, 16, 16],
        [15, 15, 15],
        [14, 14, 14],
        [13, 13, 13],
        [12, 12, 12],
        [11, 11, 11],
        [10, 10, 10],
        [9, 9, 9],
        [8, 8, 8],
        [7, 7, 7],
        [6, 6, 6],
        [5, 5, 5],
        [4, 4, 4],
        [3, 3, 3],
        [2, 2, 2],
        [1, 1, 1],
        [0, 0, 0]
    ]
    assert Solution().updateMatrix(mat) == result


def test_5():
    mat = [
        [1, 1, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    result = [
        [2, 2, 2],
        [1, 1, 1],
        [0, 0, 0]
    ]
    assert Solution().updateMatrix(mat) == result


def test_6():
    mat = [
        [1 for _ in range(10**4)]
    ]
    mat[0][-1] = 0
    result = [
        [i for i in range(10**4-1, -1, -1)]
    ]
    assert Solution().updateMatrix(mat) == result


def test_7():
    mat = [
        [1 for _ in range(4)]
    ]
    mat[0][-1] = 0
    result = [
        [i for i in range(4-1, -1, -1)]
    ]
    assert Solution().updateMatrix(mat) == result


"""
[[0,0,0],[0,1,0],[0,0,0]]
[[0,0,0],[0,1,0],[1,1,1]]
[[0],[0],[0],[0],[0]]
[[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]
[[1, 1, 1],[1, 1, 1],[0, 0, 0]]
"""
