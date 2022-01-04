from .code import Solution


def test_1():
    nums = [1, 2, 3]
    res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert Solution().permute(nums) == res


def test_2():
    nums = [0, 1]
    res = [[0, 1], [1, 0]]
    assert Solution().permute(nums) == res


def test_3():
    nums = [1]
    res = [[1]]
    assert Solution().permute(nums) == res


"""
[1, 2, 3]
[0, 1]
[1]
"""
