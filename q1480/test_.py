from .code import Solution


def test_1():
    nums = [1, 2, 3, 4]
    res = [1, 3, 6, 10]
    assert Solution().runningSum(nums) == res


def test_2():
    nums = [1, 1, 1, 1, 1]
    res = [1, 2, 3, 4, 5]
    assert Solution().runningSum(nums) == res


def test_3():
    nums = [3, 1, 2, 10, 1]
    res = [3, 4, 6, 16, 17]
    assert Solution().runningSum(nums) == res


def test_4():
    nums = [1]
    res = [1]
    assert Solution().runningSum(nums) == res


"""
"""
