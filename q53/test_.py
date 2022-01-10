from .code import Solution


def test_1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = 6
    assert Solution().maxSubArray(nums) == res


def test_2():
    nums = [1]
    res = 1
    assert Solution().maxSubArray(nums) == res


def test_3():
    nums = [5, 4, -1, 7, 8]
    res = 23
    assert Solution().maxSubArray(nums) == res


def test_4():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 6]
    res = 7
    assert Solution().maxSubArray(nums) == res


def test_5():
    nums = [-2, -3, -1, -5, -2]
    res = -1
    assert Solution().maxSubArray(nums) == res


"""
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
[1]
[5, 4, -1, 7, 8]
[-2, 1, -3, 4, -1, 2, 1, -5, 6]
"""
