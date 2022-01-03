from .code import Solution


def test_1():
    n = 4
    k = 2
    res = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ]
    assert Solution().combine(n, k) == res


def test_2():
    n = 1
    k = 1
    res = [[1]]
    assert Solution().combine(n, k) == res


def test_3():
    n = 5
    k = 3
    res = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 5],
        [3, 4, 5]
    ]
    assert Solution().combine(n, k) == res


"""
4
2
1
1
5
3
"""
