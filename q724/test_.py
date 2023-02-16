from .code import Solution


def test_1():
    nums = [1, 7, 3, 6, 5, 6]
    res = 3
    assert Solution().pivotIndex(nums) == res


def test_2():
    nums = [1, 2, 3]
    res = -1
    assert Solution().pivotIndex(nums) == res


def test_3():
    nums = [2, 1, -1]
    res = 0
    assert Solution().pivotIndex(nums) == res


def test_4():
    nums = [1, -1, 2]
    res = 2
    assert Solution().pivotIndex(nums) == res


"""
"""
