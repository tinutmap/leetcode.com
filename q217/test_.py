from .code import Solution


def test_1():
    nums = [1, 2, 3, 1]
    res = True
    assert Solution().containsDuplicate(nums) == res


def test_2():
    nums = [1, 2, 3, 4]
    res = False
    assert Solution().containsDuplicate(nums) == res


def test_3():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = True
    assert Solution().containsDuplicate(nums) == res


def test_4():
    nums = [1]
    res = False
    assert Solution().containsDuplicate(nums) == res


"""
[1, 2, 3, 1]
[1, 2, 3, 4]
[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
[1]
"""
