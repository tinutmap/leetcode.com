from .q121 import Solution


def test_1():
    prices = [7, 1, 5, 3, 6, 4]
    res = 5
    assert Solution().maxProfit(prices) == res


def test_2():
    prices = [7, 6, 4, 3, 1]
    res = 0
    assert Solution().maxProfit(prices) == res


"""
[7, 1, 5, 3, 6, 4]
[7, 6, 4, 3, 1]
"""
