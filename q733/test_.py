from .code import Solution


def test_1():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    result = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert Solution().floodFill(image, sc, sr, newColor) == result


def test_2():
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    result = [[2, 2, 2], [2, 2, 2]]
    assert Solution().floodFill(image, sc, sr, newColor) == result


def test_3():
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    result = [[0, 0, 0], [0, 1, 1]]
    assert Solution().floodFill(image, sc, sr, newColor) == result


"""
[[1,1,1],[1,1,0],[1,0,1]]
1
1
2
[[0,0,0],[0,0,0]]
0
0
2
[[0,0,0],[0,1,1]]
1
1
1
"""
