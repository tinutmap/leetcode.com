from .code import Solution


def test_1():
    s = "abccccdd"
    res = 7
    assert Solution().longestPalindrome(s) == res


def test_2():
    s = "a"
    res = 1
    assert Solution().longestPalindrome(s) == res


"""
"""
