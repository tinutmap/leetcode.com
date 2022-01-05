from .code import Solution


def test_1():
    nums = [1, 2, 3, 1]
    res = 4
    assert Solution().rob(nums) == res


def test_2():
    nums = [2, 7, 9, 3, 1]
    res = 12
    assert Solution().rob(nums) == res


def test_3():
    nums = [0]
    res = 0
    assert Solution().rob(nums) == res


"""
[1, 2, 3, 1]
[2, 7, 9, 3, 1]
[0]
"""
