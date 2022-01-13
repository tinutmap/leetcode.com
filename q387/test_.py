from .code import Solution


def test_1():
    s = "leetcode"
    res = 0
    assert Solution().firstUniqChar(s) == res


def test_2():
    s = "loveleetcode"
    res = 2
    assert Solution().firstUniqChar(s) == res


def test_3():
    s = "aabb"
    res = -1
    assert Solution().firstUniqChar(s) == res


"""
"leetcode"
"loveleetcode"
"aabb"
"""
