from .code import Solution


def test_1():
    n = 0b00000000000000000000000000001011
    result = 3
    assert(Solution().hammingWeight(n)) == result


def test_2():
    n = 0b00000000000000000000000010000000
    result = 1
    assert(Solution().hammingWeight(n)) == result


def test_3():
    n = 0b11111111111111111111111111111101
    result = 31
    assert(Solution().hammingWeight(n)) == result


def test_4():
    n = 0b00000000000000000000000000000000
    result = 0
    assert(Solution().hammingWeight(n)) == result


"""
00000000000000000000000000001011
00000000000000000000000010000000
11111111111111111111111111111101
00000000000000000000000000000000
"""
