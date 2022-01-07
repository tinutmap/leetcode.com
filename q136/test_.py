from .code import Solution


def test_1():
    nums = [2, 2, 1]
    res = 1
    assert Solution().singleNumber(nums) == res


def test_2():
    nums = [4, 1, 2, 1, 2]
    res = 4
    assert Solution().singleNumber(nums) == res


def test_3():
    nums = [1]
    res = 1
    assert Solution().singleNumber(nums) == res


"""
[2, 2, 1]
[4, 1, 2, 1, 2]
[1]
"""
