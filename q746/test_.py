from .code import Solution


def test_1():
    cost = [1, 5]
    res = 1
    assert Solution().minCostClimbingStairs(cost) == res


def test_2():
    cost = [10, 15, 20]
    res = 15
    assert Solution().minCostClimbingStairs(cost) == res


def test_3():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = 6
    assert Solution().minCostClimbingStairs(cost) == res


"""
[1, 5]
[10,15,20]
[1,100,1,1,1,100,1,1,100,1]
"""
