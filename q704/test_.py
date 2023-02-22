from q704 import Solution


def test_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    res = 4
    assert Solution().search(nums, target) == res


def test_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    res = -1
    assert Solution().search(nums, target) == res


def test_3():
    nums = [-1, 0, 3, 5, 9, 10, 12, 14]
    target = 13
    res = -1
    assert Solution().search(nums, target) == res


"""
"""
