from .code import Solution


def test_1():
    nums = [2, 7, 11, 15]
    target = 9
    res = [0, 1]
    assert Solution().twoSum(nums, target) == res


def test_2():
    nums = [3, 2, 4]
    target = 6
    res = [1, 2]
    assert Solution().twoSum(nums, target) == res


def test_3():
    nums = [3, 3]
    target = 6
    res = [0, 1]
    assert Solution().twoSum(nums, target) == res


"""
[2,7,11,15]
9
[3,2,4]
6
[3,3]
6

"""
