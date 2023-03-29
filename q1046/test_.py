from .code import Solution


def test_1():
    stones = [2, 7, 4, 1, 8, 1]
    res = 1
    assert Solution().lastStoneWeight(stones) == res


def test_2():
    stones = [1]
    res = 1
    assert Solution().lastStoneWeight(stones) == res


def test_3():
    stones = [3, 7, 8]
    res = 2
    assert Solution().lastStoneWeight(stones) == res


"""
[2,7,4,1,8,1]
[1]
"""
